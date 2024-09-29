# Write your MySQL query statement below
SELECT
e.employee_id
FROM Employees e
WHERE e.salary < 30000 AND e.manager_id AND e.manager_id NOT IN (SELECT e1.employee_id FROM Employees e1)
ORDER BY e.employee_id