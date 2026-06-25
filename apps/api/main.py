import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from models import Tle
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from ingest import ingest
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the application lifecycle,
    starts the scheduler on startup and shuts it down on exit
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(ingest, "interval", hours=int(os.getenv("TLE_FETCH_INTERVAL_HOURS", "6")))
    scheduler.start()  # starts the scheduler when the API starts
    ingest()
    yield
    scheduler.shutdown()  # properly shuts down the scheduler when the API is shut down


# registers the lifespan handler for startup/shutdown events
app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000").split(","),
    allow_methods=["GET"],
    allow_headers=["*"],
)


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
def list_tle(group: str = None, limit: int = 100, offset: int = 0 ,db: Session = Depends(get_db)):
    """ Returns all TLEs, optionally filtered by group """
    query = db.query(Tle)
    if group:
        query = query.filter(Tle.source_group == group)
    return query.offset(offset).limit(limit).all()


@app.get("/api/tle/{satellite_id}")
def get_tle(satellite_id: str, db: Session = Depends(get_db)):
    """Returns a single TLE by satellite ID, or 404 if not found"""
    tle = db.query(Tle).filter(Tle.satellite_id == satellite_id).first()
    if tle is None:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return tle
