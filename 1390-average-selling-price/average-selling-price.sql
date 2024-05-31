SELECT p.product_id, 
CASE
    WHEN SUM(u.units) is NULL THEN 0
    ELSE ROUND(SUM(p.price * u.units) / SUM(u.units), 2)
END AS average_price 
FROM Prices p 
LEFT JOIN UnitsSold u 
ON u.product_id = p.product_id AND purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id;