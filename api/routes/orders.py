from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session
from algorithms.assign_courier import assign

router = APIRouter()

class ItemIn(BaseModel):
    dish_id: int
    qty: int

class OrderIn(BaseModel):
    restaurant_id: int
    client_id: int
    items: list[ItemIn]

@router.post("/")
def create(data: OrderIn, db: Session = Depends(get_session)):
    total = 0
    for it in data.items:
        d = db.execute(text("SELECT price FROM dishes WHERE id=:i"), {"i": it.dish_id}).fetchone()
        if not d: raise HTTPException(404, f"Блюдо {it.dish_id} не найдено")
        total += d[0] * it.qty

    client = db.execute(text("SELECT lat, lon FROM clients WHERE id=:i"),
                        {"i": data.client_id}).fetchone()
    couriers = [dict(r._mapping) for r in db.execute(text("SELECT * FROM couriers WHERE available")).fetchall()]
    c = assign({"lat": float(client[0]), "lon": float(client[1])}, couriers)

    order = db.execute(text("""
        INSERT INTO orders (restaurant_id, client_id, courier_id, total, status)
        VALUES (:restaurant_id,:client_id,:courier_id,:total, 'new') RETURNING id
    """), {"restaurant_id": data.restaurant_id, "client_id": data.client_id,
           "courier_id": c['id'] if c else None, "total": total}).fetchone()

    for it in data.items:
        d = db.execute(text("SELECT price FROM dishes WHERE id=:i"), {"i": it.dish_id}).fetchone()
        db.execute(text("""
            INSERT INTO order_items (order_id, dish_id, qty, price)
            VALUES (:o, :d, :q, :p)
        """), {"o": order[0], "d": it.dish_id, "q": it.qty, "p": d[0]})

    if c:
        db.execute(text("UPDATE couriers SET available=FALSE WHERE id=:i"), {"i": c['id']})

    db.commit()
    return {"order_id": order[0], "total": total, "courier_id": c['id'] if c else None}

@router.post("/{order_id}/deliver")
def deliver(order_id: int, db: Session = Depends(get_session)):
    db.execute(text("""
        UPDATE orders SET status='done', delivered=NOW() WHERE id=:i
    """), {"i": order_id})
    db.execute(text("""
        UPDATE couriers SET available=TRUE
        WHERE id = (SELECT courier_id FROM orders WHERE id=:i)
    """), {"i": order_id})
    db.commit()
    return {"status": "delivered"}
