# Write your MySQL query statement below
WITH top_3_salaries AS (SELECT salary, departmentId,
    ROW_NUMBER() OVER(Partition BY departmentId ORDER BY salary DESC) AS rn
    FROM (SELECT departmentId, salary FROM Employee GROUP BY departmentId, salary) a
)

SELECT DISTINCT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id 
INNER JOIN top_3_salaries t ON e.salary = t.salary AND e.departmentId = t.departmentId
WHERE t.rn <= 3;