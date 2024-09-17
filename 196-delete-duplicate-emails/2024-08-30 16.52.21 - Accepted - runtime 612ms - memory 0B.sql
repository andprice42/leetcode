# Write your MySQL query statement below
DELETE FROM Person p1 WHERE p1.id IN (
    SELECT id FROM (SELECT id, ROW_NUMBER() OVER(PARTITION BY email ORDER BY id ASC) AS rn FROM Person) a WHERE rn > 1
);
