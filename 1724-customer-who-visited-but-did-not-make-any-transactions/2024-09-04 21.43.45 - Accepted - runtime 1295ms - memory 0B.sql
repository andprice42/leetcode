# Write your MySQL query statement below
WITH cte AS (
    SELECT v.visit_id
    FROM Visits v INNER JOIN Transactions t ON v.visit_id = t.visit_id
)
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
WHERE v.visit_id NOT IN (SELECT * FROM cte)
GROUP BY v.customer_id