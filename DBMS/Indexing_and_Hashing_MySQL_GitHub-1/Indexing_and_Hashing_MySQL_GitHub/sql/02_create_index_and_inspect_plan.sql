-- Experiment 2: Create an index and inspect the plan
USE IndexHashLab;

CREATE INDEX idx_student_id
ON Students_NoIndex(Student_ID);

EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE Student_ID = 107;

SHOW INDEX FROM Students_NoIndex;
