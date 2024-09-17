# Write your MySQL query statement below
WITH cte AS (
    SELECT b.student_id
    ,b.subject_name
    ,CASE WHEN e.subject_name IS NULL THEN 0 ELSE 1 END AS cnt
    FROM
    (
        SELECT
        st.student_id
        ,s.subject_name
        FROM Students st, Subjects s
    ) b LEFT JOIN Examinations e ON b.student_id = e.student_id AND b.subject_name = e.subject_name
)
SELECT 
s.student_id
,s.student_name
,c.subject_name
,SUM(cnt) AS attended_exams
FROM cte c
JOIN Students s ON c.student_id = s.student_id
GROUP BY s.student_id, s.student_name, c.subject_name
ORDER BY s.student_id, c.subject_name


