import os
import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from models import Tle
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from ingest import ingest
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the application lifecycle: starts the background scheduler,
    attempts an initial TLE ingestion and shuts the scheduler down on exit
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(ingest, "interval", hours=int(os.getenv("TLE_FETCH_INTERVAL_HOURS", "6")))
    scheduler.start()
    try:
        ingest()
    except Exception as e:
        logging.warning("Startup ingestion failed, will retry on next schedule: %s", e)
    yield
    scheduler.shutdown()

limiter = Limiter(key_func=get_remote_address)


# security headers
class SecurityHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response


# registers the lifespan handler for startup/shutdown events
app = FastAPI(lifespan=lifespan)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000").split(","),
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.add_middleware(SecurityHeaderMiddleware)


def get_db():
    """
    opens a database session,
    passes it to the route,
    and then automatically closes it afterward
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health(db: Session = Depends(get_db)):
    """ Checks that the API is running and the database responds """
    db.execute(text("SELECT 1"))
    return {"status": "okay"}


@app.get("/api/tle")
@limiter.limit("60/minute")
def list_tle(request: Request, group: str = None, limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    """ Returns all TLEs, optionally filtered by group """
    query = db.query(Tle)
    if group:
        query = query.filter(Tle.source_group == group)
    return query.offset(offset).limit(limit).all()


@app.get("/api/tle/{satellite_id}")
@limiter.limit("60/minute")
def get_tle(request: Request, satellite_id: str, db: Session = Depends(get_db)):
    """Returns a single TLE by satellite ID, or 404 if not found"""
    tle = db.query(Tle).filter(Tle.satellite_id == satellite_id).order_by(Tle.ingested_at.desc()).first()
    if tle is None:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return tle
