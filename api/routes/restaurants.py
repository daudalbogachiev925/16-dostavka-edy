from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class RIn(BaseModel):
    name: str
    city: str | None = None
    lat: float
    lon: float

@router.post("/")
def create(data: RIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO restaurants (name, city, lat, lon)
        VALUES (:name,:city,:lat,:lon) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(city: str | None = None, db: Session = Depends(get_session)):
    sql = "SELECT * FROM restaurants"
    params = {}
    if city:
        sql += " WHERE city = :c"
        params['c'] = city
    return [dict(r._mapping) for r in db.execute(text(sql), params).fetchall()]
