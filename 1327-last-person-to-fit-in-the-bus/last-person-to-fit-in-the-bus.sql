WITH TWT AS (
    SELECT *, SUM(weight) OVER (ORDER BY turn) AS totalWeight
    FROM Queue
    ORDER BY turn
)
SELECT person_name
FROM Queue q
WHERE q.turn = (
    SELECT MAX(turn) 
    FROM TWT 
    WHERE totalWeight <= 1000
);