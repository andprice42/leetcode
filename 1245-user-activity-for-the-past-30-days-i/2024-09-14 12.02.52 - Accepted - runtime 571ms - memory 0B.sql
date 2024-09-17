# Write your MySQL query statement below
SELECT
activity_date AS day
,COUNT(DISTINCT user_id) AS active_users
FROM Activity a
WHERE a.activity_date > DATE '2019-06-27' AND a.activity_date < DATE '2019-07-28'
GROUP BY a.activity_date