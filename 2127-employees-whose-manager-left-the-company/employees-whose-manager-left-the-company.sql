SELECT employee_id 
FROM Employees 
WHERE salary < 30000 AND
    NOT manager_id IN (
        SELECT DISTINCT employee_id
        FROM Employees
    )
ORDER BY employee_id