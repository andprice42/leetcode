# Write your MySQL query statement below
WITH filt_logs AS (
SELECT
LAG(id, 2, NULL) OVER(ORDER BY id) AS id_1
,LAG(num, 2, NULL) OVER(ORDER BY id) AS num_1
,LAG(id, 1, NULL) OVER(ORDER BY id) AS id_2
,LAG(num, 1, NULL) OVER(ORDER BY id) AS num_2
,id AS id_3
,num AS num_3
FROM Logs
)
SELECT DISTINCT num_3 AS ConsecutiveNums
FROM filt_logs
WHERE num_3 = num_1 AND num_3 = num_2