# Write your MySQL query statement below
WITH cte AS (
SELECT
CASE WHEN income < 20000 THEN 'Low Salary'
     WHEN income <= 50000 THEN 'Average Salary'
     ELSE 'High Salary' END AS category
,1 AS sal_cat_cnt
FROM Accounts a
),
cte2 AS (
    SELECT * FROM cte
    UNION ALL
    SELECT 'Low Salary' AS category, 0 AS sal_cat_cnt
    UNION ALL
    SELECT 'Average Salary' AS category, 0 AS sal_cat_cnt
    UNION ALL
    SELECT 'High Salary' AS category, 0 AS sal_cat_cnt
)
SELECT
category
,SUM(sal_cat_cnt) AS accounts_count
FROM cte2
GROUP BY category