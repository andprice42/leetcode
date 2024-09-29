# Write your MySQL query statement below
SELECT 
ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance i
WHERE i.tiv_2015 IN (SELECT i1.tiv_2015 FROM Insurance i1 WHERE i1.pid <> i.pid)
AND CONCAT(i.lat, " - ", i.lon) NOT IN (SELECT CONCAT(i2.lat, " - ", i2.lon) FROM Insurance i2 WHERE i2.pid <> i.pid)