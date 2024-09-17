# Write your MySQL query statement below
WITH cte AS (
    SELECT
    machine_id
    ,process_id
    ,activity_type
    ,LEAD(timestamp, 1, 0) OVER(ORDER BY machine_id, process_id, activity_type) - timestamp AS delta
    FROM Activity
)
SELECT machine_id, ROUND(AVG(delta), 3) AS processing_time
FROM cte
WHERE activity_type = 'start'
GROUP BY machine_id