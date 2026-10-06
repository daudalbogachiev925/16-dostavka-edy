from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/top")
def top(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/top_restaurants.sql').read())).fetchall()]

@router.get("/couriers")
def couriers(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/courier_kpi.sql').read())).fetchall()]

@router.get("/delivery-time")
def delivery_time(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/delivery_time.sql').read())).fetchall()]

@router.get("/revenue")
def revenue(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/revenue.sql').read())).fetchall()]
