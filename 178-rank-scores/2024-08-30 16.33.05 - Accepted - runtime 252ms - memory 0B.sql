# Write your MySQL query statement below
WITH rankings AS (
    SELECT score, ROW_NUMBER() OVER(ORDER BY score DESC) AS rnk FROM (
    SELECT DISTINCT score FROM Scores) c
)

SELECT a.score, b.rnk AS 'rank' FROM Scores a INNER JOIN rankings b ON a.score = b.score
ORDER BY a.score DESC;