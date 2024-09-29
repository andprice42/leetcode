# Write your MySQL query statement below
WITH daily_sums AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
),
get_averages AS (
    SELECT
    visited_on
    ,ROW_NUMBER() OVER(ORDER BY visited_on) AS row_num
    ,SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
    ,AVG(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount
    FROM daily_sums
)
SELECT visited_on, amount, ROUND(average_amount, 2) AS average_amount 
FROM get_averages
WHERE row_num >= 7