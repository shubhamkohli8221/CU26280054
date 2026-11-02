-- Experiment 4: Composite index and leftmost-prefix rule
USE IndexHashLab;

CREATE INDEX idx_department_name
ON Students_NoIndex(Department, Student_Name);

-- Uses the leftmost column
EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE Department = 'MCA';

-- Can use both indexed columns
EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE Department = 'MCA'
  AND Student_Name = 'Aman';

-- The composite index alone is not normally a direct lookup
-- for the second column without the leftmost column
EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE Student_Name = 'Aman';
