# Write your MySQL query statement below
WITH cte AS (
    SELECT
    s.product_id
    ,MIN(s.year) AS year
    FROM Sales s
    GROUP BY s.product_id
)
SELECT s.product_id, s.year AS first_year, sa.quantity, sa.price
FROM cte s INNER JOIN Sales sa ON s.product_id = sa.product_id AND s.year = sa.year