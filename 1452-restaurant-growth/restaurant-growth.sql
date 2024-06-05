WITH dailyAmount AS (
    SELECT visited_on, SUM(amount) AS day_sum 
    FROM Customer 
    GROUP BY visited_on
)
SELECT d1.visited_on AS visited_on, SUM(d2.day_sum) AS amount,
    ROUND(AVG(d2.day_sum), 2) AS average_amount
FROM dailyAmount d1, dailyAmount d2
WHERE DATEDIFF(d1.visited_on, d2.visited_on) BETWEEN 0 AND 6
GROUP BY d1.visited_on
HAVING COUNT(d2.visited_on) = 7