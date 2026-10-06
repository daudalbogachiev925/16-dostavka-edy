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
    db.execute(text("UPDATE couriers SET lat=:lat, lon=:lon WHERE id=:i"),
               {"lat": lat, "lon": lon, "i": courier_id})
    db.commit()
    return {"status": "updated"}

@router.get("/")
def list_all(available: bool | None = None, db: Session = Depends(get_session)):
    sql = "SELECT * FROM couriers"
    params = {}
    if available is not None:
        sql += " WHERE available = :a"
        params['a'] = available
    return [dict(r._mapping) for r in db.execute(text(sql), params).fetchall()]
