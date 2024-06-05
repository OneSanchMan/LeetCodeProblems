SELECT name as results
FROM (
    SELECT name, COUNT(*) AS rating_count
    FROM MovieRating
    JOIN Users
    ON MovieRating.user_id = Users.user_id
    GROUP BY MovieRating.user_id
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
) AS RatingCounter
UNION ALL
SELECT title
FROM (
    SELECT title, AVG(rating) AS avgRating
    FROM MovieRating
    JOIN Movies 
    ON Movies.movie_id = MovieRating.movie_id
    WHERE created_at BETWEEN "2020-02-01" AND "2020-02-29"
    GROUP BY MovieRating.movie_id
    ORDER BY avgRating DESC, title ASC
    LIMIT 1
) AS FebRating