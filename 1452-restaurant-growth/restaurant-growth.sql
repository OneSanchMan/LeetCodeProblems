SELECT s1.visited_on AS visited_on, SUM(s2.day_sum) AS amount,
    ROUND(AVG(s2.day_sum), 2) AS average_amount
FROM (
    SELECT visited_on, SUM(amount) AS day_sum 
    FROM Customer 
    GROUP BY visited_on ) s1, 
    (
    SELECT visited_on, SUM(amount) AS day_sum 
    FROM Customer 
    GROUP BY visited_on ) s2
WHERE DATEDIFF(s1.visited_on, s2.visited_on) BETWEEN 0 AND 6
GROUP BY s1.visited_on
HAVING COUNT(s2.visited_on) = 7