-- Experiment 6: Equality versus range search on the hash index
USE IndexHashLab;

-- Equality lookup: suitable for a hash index
EXPLAIN
SELECT *
FROM Students_Hash
WHERE Student_ID = 103;

-- Range query: a hash index cannot provide an ordered range lookup
EXPLAIN
SELECT *
FROM Students_Hash
WHERE Student_ID BETWEEN 101 AND 104;
