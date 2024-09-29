# Write your MySQL query statement below
SELECT
p.product_name
,SUM(o.unit) AS unit
FROM Orders o INNER JOIN Products p ON o.product_id = p.product_id
WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 2
GROUP BY o.product_id, p.product_name
HAVING SUM(o.unit) >= 100