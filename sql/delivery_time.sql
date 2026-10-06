SELECT o.id, r.name AS restaurant, c.name AS client,
       EXTRACT(EPOCH FROM (o.delivered - o.created))/60 AS minutes
FROM orders o
JOIN restaurants r ON r.id = o.restaurant_id
JOIN clients c ON c.id = o.client_id
WHERE o.status = 'done'
ORDER BY minutes DESC
LIMIT 20;
