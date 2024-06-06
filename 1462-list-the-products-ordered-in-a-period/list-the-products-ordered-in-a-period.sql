WITH FebOrders AS (
    SELECT *
    FROM Orders
    WHERE order_date BETWEEN "2020-02-01" AND "2020-02-29"
) 
SELECT product_name, SUM(unit) AS unit
FROM Products p
JOIN FebOrders f
ON p.product_id = f.product_id
GROUP BY p.product_id
HAVING unit >= 100