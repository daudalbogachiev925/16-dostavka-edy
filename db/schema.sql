CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    address TEXT,
    lat NUMERIC(9,6),
    lon NUMERIC(9,6),
    rating NUMERIC(3,2) DEFAULT 0
);

CREATE TABLE dishes (
    id BIGSERIAL PRIMARY KEY,
    restaurant_id INT REFERENCES restaurants(id),
    name TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    category TEXT
);

CREATE TABLE clients (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    address TEXT,
    lat NUMERIC(9,6),
    lon NUMERIC(9,6)
);

CREATE TABLE couriers (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    lat NUMERIC(9,6),
    lon NUMERIC(9,6),
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE orders (
    id BIGSERIAL PRIMARY KEY,
    restaurant_id INT REFERENCES restaurants(id),
    client_id BIGINT REFERENCES clients(id),
    courier_id BIGINT REFERENCES couriers(id),
    total NUMERIC(10,2),
    delivery_fee NUMERIC(10,2) DEFAULT 0,
    status TEXT DEFAULT 'new',
    created TIMESTAMP DEFAULT NOW(),
    delivered TIMESTAMP
);

CREATE TABLE order_items (
    order_id BIGINT REFERENCES orders(id) ON DELETE CASCADE,
    dish_id BIGINT REFERENCES dishes(id),
    qty INT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    PRIMARY KEY (order_id, dish_id)
);

CREATE INDEX idx_orders_courier ON orders(courier_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created ON orders(created);
