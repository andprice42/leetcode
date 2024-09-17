# Write your MySQL query statement below
WITH cte AS (
    SELECT
    product_id
    ,MAX(change_date) AS change_date
    FROM Products p
    WHERE change_date < '2019-08-17'
    GROUP BY product_id
),
cte2 AS (
    SELECT p1.product_id, 10 
    FROM Products p1
    EXCEPT
    SELECT p.product_id, 10 FROM cte p
)
SELECT
p1.product_id
,p1.new_price AS price
FROM Products p1 INNER JOIN cte c ON p1.product_id = c.product_id AND p1.change_date = c.change_date
UNION ALL
SELECT * FROM cte2
