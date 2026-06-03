from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal

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
