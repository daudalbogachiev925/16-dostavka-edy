from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class DIn(BaseModel):
    restaurant_id: int
    name: str
    price: float
    category: str | None = None

@router.post("/")
def create(data: DIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO dishes (restaurant_id, name, price, category)
        VALUES (:restaurant_id,:name,:price,:category) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/restaurant/{restaurant_id}")
def by_restaurant(restaurant_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT * FROM dishes WHERE restaurant_id=:r
    """), {"r": restaurant_id}).fetchall()]
