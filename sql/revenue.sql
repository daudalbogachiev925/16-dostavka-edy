SELECT date_trunc('day', created) AS day,
       COUNT(*) AS orders,
       SUM(total) AS revenue,
       AVG(total) AS avg_check
FROM orders
WHERE status = 'done' AND created >= NOW() - INTERVAL '30 days'
GROUP BY day
ORDER BY day DESC;
