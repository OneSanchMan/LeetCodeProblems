WITH CT AS (
    SELECT *,
    CASE
        WHEN income < 20000 THEN "Low Salary"
        WHEN income >= 20000 AND income <= 50000 THEN "Average Salary"
        ELSE "High Salary"
    END AS category
    FROM Accounts
),
Categories AS (
    SELECT "Low Salary" AS category
    UNION 
    SELECT "Average Salary" AS category
    UNION 
    SELECT "High Salary" AS category
)

SELECT Categories.category, COUNT(account_id) AS accounts_count 
FROM CT
RIGHT JOIN Categories
ON Categories.category = CT.category
GROUP BY Categories.category