SELECT DISTINCT(one.num) AS ConsecutiveNums 
FROM Logs one
JOIN Logs two
ON one.id = two.id + 1
JOIN Logs three
ON one.id = three.id + 2
WHERE one.num = two.num AND one.num = three.num