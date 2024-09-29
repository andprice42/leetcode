# Write your MySQL query statement below
SELECT LEAD(salary, 1, NULL) OVER(ORDER BY salary DESC) AS SecondHighestSalary
 FROM (
    SELECT DISTINCT salary FROM Employee
    ) a
LIMIT 1

