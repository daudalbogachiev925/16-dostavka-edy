SELECT c.id, c.name,
       COUNT(o.id) AS deliveries,
       COUNT(o.id) FILTER (WHERE o.status='done') AS completed,
       ROUND(AVG(EXTRACT(EPOCH FROM (o.delivered - o.created))/60), 1) AS avg_minutes
FROM couriers c
LEFT JOIN orders o ON o.courier_id = c.id
GROUP BY c.id
ORDER BY deliveries DESC;
