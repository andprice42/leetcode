# Write your MySQL query statement below
WITH max_sal AS (
    SELECT departmentId AS did, MAX(salary) AS salary FROM Employee GROUP BY departmentId
)
SELECT d.name AS Department, e.name AS Employee, e.Salary AS Salary
FROM Employee e 
INNER JOIN Department d ON e.departmentId = d.id
INNER JOIN max_sal m ON e.Salary = m.salary AND e.departmentId = m.did;
