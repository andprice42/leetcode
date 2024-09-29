# Write your MySQL query statement below
WITH requester_sum AS (
    SELECT requester_id AS id, COUNT(*) AS cnt
    FROM RequestAccepted
    GROUP BY requester_id
    UNION ALL
    SELECT accepter_id AS id, COUNT(*) AS cnt
    FROM RequestAccepted
    GROUP BY accepter_id
)
SELECT id, SUM(cnt) AS num
FROM requester_sum
GROUP BY id
ORDER BY num DESC
LIMIT 1