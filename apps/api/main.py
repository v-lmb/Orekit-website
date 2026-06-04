from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from models import Tle

app = FastAPI()


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
    db.execute(text("SELECT 1"))
    return {"status": "okay"}


@app.get("/api/tle")
def list_tle(group: str = None, db: Session = Depends(get_db)):
    query = db.query(Tle)
    if group:
        query = query.filter(Tle.source_group == group)
    return query.all()


@app.get("/api/tle/{satellite_id}")
def get_tle(satellite_id: str, db: Session = Depends(get_db)):
    tle = db.query(Tle).filter(Tle.satellite_id == satellite_id).first()
    if tle is None:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return tle
