# Write your MySQL query statement below

WITH manager_ids AS (
    SELECT
    e.managerId
    FROM Employee e
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)
SELECT e.name
FROM Employee e INNER JOIN manager_ids m ON e.id = m.managerId

