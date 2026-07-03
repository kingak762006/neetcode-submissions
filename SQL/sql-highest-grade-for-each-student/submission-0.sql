SELECT e1.student_id,
       e1.exam_id,
       e1.score
FROM exam_results e1
WHERE e1.exam_id = (
    SELECT MIN(e2.exam_id)
    FROM exam_results e2
    WHERE e2.student_id = e1.student_id
      AND e2.score = (
          SELECT MAX(e3.score)
          FROM exam_results e3
          WHERE e3.student_id = e1.student_id
      )
)
ORDER BY e1.student_id;