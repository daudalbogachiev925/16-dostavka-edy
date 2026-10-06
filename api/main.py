from fastapi import FastAPI
from routes import restaurants, dishes, clients, couriers, orders, reports

app = FastAPI(title="Food Delivery API")
app.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"])
app.include_router(dishes.router, prefix="/dishes", tags=["dishes"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(couriers.router, prefix="/couriers", tags=["couriers"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def health(): return {"status": "ok"}
