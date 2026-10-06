from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class CIn(BaseModel):
    name: str
    phone: str | None = None
    lat: float
    lon: float

@router.post("/")
def create(data: CIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO couriers (name, phone, lat, lon)
        VALUES (:name,:phone,:lat,:lon) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.post("/{courier_id}/location")
def update_location(courier_id: int, lat: float, lon: float, db: Session = Depends(get_session)):
