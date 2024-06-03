SELECT MAX(singleNum) as num
FROM (
    SELECT num AS singleNum
    FROM MyNumbers 
    GROUP BY num
    HAVING COUNT(*) = 1
) AS subq