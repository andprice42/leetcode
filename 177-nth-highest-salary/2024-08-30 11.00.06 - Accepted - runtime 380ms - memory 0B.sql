CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
   WITH cte AS (SELECT DISTINCT salary FROM Employee)
   SELECT salary FROM 
        (
            SELECT salary, ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num FROM cte b
        ) a WHERE row_num = N
  );
END