CREATE OR REPLACE VIEW at_risk_students AS
WITH att AS (
    SELECT reg_no,
           ROUND(100.0 * SUM(CASE WHEN status = 'P' THEN 1 ELSE 0 END)
                 / COUNT(status), 1) AS attendance_pct
    FROM attendance
    GROUP BY reg_no
),
mk AS (
    SELECT reg_no,
           ROUND(AVG(internal_1)::numeric, 1) AS avg_internal_1,
           ROUND(AVG(internal_2)::numeric, 1) AS avg_internal_2,
           ROUND((COALESCE(SUM(internal_1), 0) + COALESCE(SUM(internal_2), 0))::numeric
                 / NULLIF(COUNT(internal_1) + COUNT(internal_2), 0), 1) AS avg_mark
    FROM marks
    GROUP BY reg_no
)
SELECT s.reg_no, s.name, att.attendance_pct,
       mk.avg_internal_1, mk.avg_internal_2, mk.avg_mark,
       (mk.avg_internal_2 < mk.avg_internal_1) AS marks_falling
FROM students s
JOIN att ON att.reg_no = s.reg_no
JOIN mk  ON mk.reg_no  = s.reg_no
WHERE att.attendance_pct < 65
  AND mk.avg_mark < 12;