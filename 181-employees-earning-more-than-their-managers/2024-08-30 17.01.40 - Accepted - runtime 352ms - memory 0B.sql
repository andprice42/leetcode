# Write your MySQL query statement below
WITH manager_salaries AS (
    SELECT id, salary FROM Employee
    WHERE id IN (SELECT DISTINCT managerId FROM Employee)
)
SELECT e.name AS Employee FROM Employee e INNER JOIN manager_salaries m ON e.managerId = m.id
WHERE e.salary > m.salary;