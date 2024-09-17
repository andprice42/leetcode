# Write your MySQL query statement below
-- WITH ordered_dates AS (
--     SELECT * FROM Weather ORDER BY id, recordDate
-- )
SELECT id FROM (SELECT id,
LAG(temperature, 1, NULL) OVER (ORDER BY recordDate) AS prev_temp,
recordDate AS curr_day,
LAG(recordDate, 1, NULL) OVER (ORDER BY recordDate) AS prev_day,
temperature AS curr_temp
FROM Weather
ORDER BY recordDate) a
WHERE a.prev_temp IS NOT NULL AND a.curr_temp > a.prev_temp AND DATEDIFF(curr_day, prev_day) = 1;