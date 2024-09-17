# Write your MySQL query statement below
WITH CTE AS (
    SELECT
    q.query_name
    ,ROUND(AVG(q.rating/q.position), 2) AS quality
    ,SUM(CASE WHEN q.rating < 3 THEN 1 ELSE 0 END) AS poor_query_cnt
    ,COUNT(*) AS query_cnt
    FROM Queries q
    GROUP BY q.query_name
)
SELECT 
query_name
,quality
,ROUND(100*poor_query_cnt/query_cnt, 2) AS poor_query_percentage
FROM CTE
WHERE query_name IS NOT NULL