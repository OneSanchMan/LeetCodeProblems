WITH CTE AS (
    SELECT name, salary, departmentId, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS top
    FROM Employee
)
SELECT Department.name AS Department, CTE.name AS Employee, salary AS Salary
FROM CTE
JOIN Department
ON CTE.departmentId = Department.id
WHERE top <= 3