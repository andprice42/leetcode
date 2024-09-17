# Write your MySQL query statement below
WITH cte AS (
    SELECT
    s.product_id
    ,s.year
    ,MIN(s.year) OVER(PARTITION BY s.product_id) AS min_year
    ,s.quantity
    ,s.price
    FROM Sales s
)
SELECT product_id, year AS first_year, quantity, price
FROM cte
WHERE year = min_year
