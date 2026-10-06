from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class CIn(BaseModel):
    name: str
    phone: str | None = None
    lat: float | None = None
    lon: float | None = None
    address: str | None = None

@router.post("/")
def create(data: CIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO clients (name, phone, lat, lon, address)
        VALUES (:name,:phone,:lat,:lon,:address) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("SELECT * FROM clients")).fetchall()]
