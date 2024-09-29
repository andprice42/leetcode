# Write your MySQL query statement below
WITH most_ratings AS (
    SELECT
    mr.user_id
    ,u.name
    ,COUNT(*) AS cnt
    FROM MovieRating mr INNER JOIN Users u ON mr.user_id = u.user_id
    GROUP BY mr.user_id, u.name
    ORDER BY cnt DESC, u.name ASC
    LIMIT 1
),
avg_mv_ratings AS (
    SELECT
    mr.movie_id
    ,m.title AS name
    ,AVG(rating) AS movie_avg
    FROM MovieRating mr LEFT JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE MONTH(created_at) = 2 AND YEAR(created_at) = 2020
    GROUP BY mr.movie_id, m.title
    ORDER BY movie_avg DESC, m.title ASC
    LIMIT 1
)
SELECT name AS results FROM most_ratings
UNION ALL
SELECT name AS results FROM avg_mv_ratings