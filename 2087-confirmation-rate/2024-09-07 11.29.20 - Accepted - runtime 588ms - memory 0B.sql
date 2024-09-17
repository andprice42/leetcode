# Write your MySQL query statement below
WITH combined AS(
    SELECT
    s.user_id
    ,SUM(CASE WHEN c.action IS NULL OR c.action = 'timeout' THEN 0 ELSE 1 END) AS confirmed
    ,COUNT(*) AS requests
    FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id
    GROUP BY s.user_id
)
SELECT
user_id
,ROUND(confirmed/requests, 2) AS confirmation_rate
FROM combined