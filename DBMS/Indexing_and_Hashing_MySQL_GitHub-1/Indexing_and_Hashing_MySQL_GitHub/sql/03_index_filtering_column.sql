-- Experiment 3: Index a filtering column
USE IndexHashLab;

EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE City = 'Jaipur';

CREATE INDEX idx_student_city
ON Students_NoIndex(City);

EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE City = 'Jaipur';
