-- Experiment 8: Drop an index and compare
USE IndexHashLab;

DROP INDEX idx_student_city
ON Students_NoIndex;

EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE City = 'Jaipur';
