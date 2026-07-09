SELECT s.student_id,s.student_name,f.subject_name,COUNT(e.student_id) AS attended_exams
FROM Students s
Cross JOIN Subjects f
LEFT JOIN Examinations e 
ON s.student_id = e.student_id
AND f.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, f.subject_name
order by s.student_id, f.subject_name;