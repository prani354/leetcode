# Write your MySQL query statement below
SELECT s.student_id,s.student_name,f.subject_name,COUNT(e.subject_name) AS attended_exams
FROM Students s
JOIN Subjects f
LEFT JOIN Examinations e 
ON s.student_id = e.student_id
AND f.subject_name = e.subject_name
GROUP BY s.student_id,f.subject_name
ORDER BY student_id ASC, subject_name ASC;
