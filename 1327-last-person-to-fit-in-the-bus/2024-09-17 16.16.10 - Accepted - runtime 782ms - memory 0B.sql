# Write your MySQL query statement below
WITH cte AS (
    SELECT
    person_id
    ,person_name
    ,SUM(weight) OVER(ORDER BY turn) AS rolling_sum
    ,turn
    FROM Queue q
    ORDER BY turn
)
SELECT person_name
FROM cte
WHERE rolling_sum <= 1000
ORDER BY turn DESC
LIMIT 1
