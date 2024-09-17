# Write your MySQL query statement below
-- SELECT id FROM (SELECT id,
-- LAG(temperature, 1, NULL) OVER (ORDER BY recordDate) AS prev_temp,
-- recordDate AS curr_day,
-- LAG(recordDate, 1, NULL) OVER (ORDER BY recordDate) AS prev_day,
-- temperature AS curr_temp
-- FROM Weather
-- ORDER BY recordDate) a
-- WHERE a.prev_temp IS NOT NULL AND a.curr_temp > a.prev_temp AND DATEDIFF(curr_day, prev_day) = 1;
WITH cte AS (
    SELECT id
    ,recordDate AS curr_date
    ,LAG(recordDate, 1, 0) OVER(ORDER BY recordDate) AS prev_date
    ,temperature AS curr_temp
    ,LAG(temperature, 1, 0) OVER(ORDER BY recordDate) AS prev_temp
    FROM Weather
)
SELECT id FROM cte 
WHERE curr_temp > prev_temp AND DATEDIFF(curr_date, prev_date) = 1
