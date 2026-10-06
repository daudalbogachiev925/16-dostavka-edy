SELECT r.id, r.name, r.rating,
       COUNT(o.id) AS orders,
       SUM(o.total) AS revenue,
       ROUND(AVG(o.total),2) AS avg_check
FROM restaurants r
LEFT JOIN orders o ON o.restaurant_id = r.id AND o.status='done'
GROUP BY r.id
ORDER BY revenue DESC NULLS LAST;
