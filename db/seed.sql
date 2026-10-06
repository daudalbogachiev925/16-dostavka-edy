INSERT INTO restaurants (name, city, lat, lon, rating) VALUES
('Пицца-Хаус','Москва',55.7558,37.6173,4.7),
('Суши-Мастер','Москва',55.7700,37.6000,4.5),
('Бургер-Кинг','СПб',59.9343,30.3351,4.3);

INSERT INTO dishes (restaurant_id, name, price, category) VALUES
(1,'Пицца Маргарита',600,'пицца'),(1,'Пицца Пепперони',750,'пицца'),
(2,'Ролл Калифорния',400,'суши'),(2,'Сет Филадельфия',1200,'суши'),
(3,'Бургер Классик',300,'бургеры'),(3,'Картошка',150,'гарнир');

INSERT INTO clients (name, phone, lat, lon) VALUES
('Аня','+7900',55.7600,37.6200),
('Петя','+7901',55.7700,37.6100),
('Катя','+7902',55.7500,37.6300);

INSERT INTO couriers (name, phone, lat, lon, available) VALUES
('Иван','+7910',55.7550,37.6180,TRUE),
('Сергей','+7911',55.7650,37.6100,TRUE),
('Дмитрий','+7912',55.7400,37.6400,TRUE);

INSERT INTO orders (restaurant_id, client_id, courier_id, total, status) VALUES
(1,1,1,1350,'done'),
(2,2,2,1200,'done'),
(1,3,1,600,'in_progress'),
(3,1,3,450,'new');
