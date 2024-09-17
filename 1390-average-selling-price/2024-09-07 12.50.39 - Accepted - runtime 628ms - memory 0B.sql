# Write your MySQL query statement below
WITH cte AS (
    SELECT
    u.product_id
    ,SUM(u.units) AS units_sum
    ,SUM(u.units*(SELECT p.price FROM Prices p WHERE p.product_id = u.product_id AND p.start_date <= u.purchase_date AND p.end_date >= u.purchase_date LIMIT 1)) AS total_cost
    FROM UnitsSold u
    GROUP BY u.product_id
)
SELECT
DISTINCT
p.product_id
,CASE WHEN c.total_cost IS NULL THEN 0 ELSE ROUND(c.total_cost/c.units_sum, 2) END AS average_price
FROM Prices p LEFT JOIN cte c ON p.product_id = c.product_id