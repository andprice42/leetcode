# Write your MySQL query statement below

SELECT ROUND(COUNT(DISTINCT c.player_id)/(SELECT COUNT(DISTINCT a1.player_id) FROM Activity a1), 2) AS Fraction
FROM
(SELECT player_id
FROM
    (
        SELECT
        player_id
        ,event_date
        ,LEAD(event_date, 1, NULL) OVER(PARTITION BY player_id ORDER BY player_id, event_date) AS edate
        FROM
        (
        SELECT
        player_id
        ,event_date
        ,ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS row_num
        FROM Activity
        ORDER BY player_id, event_date
        ) a
        WHERE row_num < 3
    ) b
WHERE DATEDIFF(edate, event_date) = 1 
) c
