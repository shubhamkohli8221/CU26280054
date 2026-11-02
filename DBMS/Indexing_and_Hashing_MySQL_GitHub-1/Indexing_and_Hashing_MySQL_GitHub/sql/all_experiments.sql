-- DBMS Lab: Indexing and Hashing Using MySQL 8.0\n-- Run this file once, from start to finish, in MySQL.\n\n\n-- ========================================================================\n-- 01_create_table_without_index.sql\n-- ========================================================================\n-- Experiment 1: Create a table without an index
CREATE DATABASE IF NOT EXISTS IndexHashLab;
USE IndexHashLab;

CREATE TABLE Students_NoIndex (
    Student_ID INT NOT NULL,
    Student_Name VARCHAR(50),
    Department VARCHAR(30),
    City VARCHAR(30)
) ENGINE = InnoDB;

INSERT INTO Students_NoIndex VALUES
(101, 'Ravi', 'MCA', 'Jaipur'),
(102, 'Priya', 'BCA', 'Delhi'),
(103, 'Aman', 'MCA', 'Jaipur'),
(104, 'Neha', 'BCA', 'Mumbai'),
(105, 'Karan', 'MCA', 'Delhi'),
(106, 'Simran', 'BCA', 'Jaipur'),
(107, 'Arjun', 'MCA', 'Mumbai'),
(108, 'Meera', 'BCA', 'Delhi'),
(109, 'Rahul', 'MCA', 'Jaipur'),
(110, 'Pooja', 'BCA', 'Mumbai');

SELECT * FROM Students_NoIndex;

EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE Student_ID = 107;
\n\n-- ========================================================================\n-- 02_create_index_and_inspect_plan.sql\n-- ========================================================================\n-- Experiment 2: Create an index and inspect the plan
USE IndexHashLab;

CREATE INDEX idx_student_id
ON Students_NoIndex(Student_ID);

EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE Student_ID = 107;

SHOW INDEX FROM Students_NoIndex;
\n\n-- ========================================================================\n-- 03_index_filtering_column.sql\n-- ========================================================================\n-- Experiment 3: Index a filtering column
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
\n\n-- ========================================================================\n-- 04_composite_index_leftmost_prefix.sql\n-- ========================================================================\n-- Experiment 4: Composite index and leftmost-prefix rule
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
\n\n-- ========================================================================\n-- 05_hash_index_using_memory.sql\n-- ========================================================================\n-- Experiment 5: Create a hash index using MEMORY
USE IndexHashLab;

CREATE TABLE Students_Hash (
    Student_ID INT NOT NULL,
    Student_Name VARCHAR(50),
    Department VARCHAR(30),
    INDEX idx_hash_student_id (Student_ID) USING HASH
) ENGINE = MEMORY;

INSERT INTO Students_Hash VALUES
(101, 'Ravi', 'MCA'),
(102, 'Priya', 'BCA'),
(103, 'Aman', 'MCA'),
(104, 'Neha', 'BCA'),
(105, 'Karan', 'MCA');

SELECT * FROM Students_Hash;

SHOW INDEX FROM Students_Hash;

EXPLAIN
SELECT *
FROM Students_Hash
WHERE Student_ID = 103;
\n\n-- ========================================================================\n-- 06_hash_index_equality_vs_range.sql\n-- ========================================================================\n-- Experiment 6: Equality versus range search on the hash index
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
\n\n-- ========================================================================\n-- 07_inspect_innodb_index.sql\n-- ========================================================================\n-- Experiment 7: Inspect an InnoDB index
USE IndexHashLab;

CREATE TABLE Students_InnoDB (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(50),
    Department VARCHAR(30)
) ENGINE = InnoDB;

CREATE INDEX idx_innodb_name
ON Students_InnoDB(Student_Name);

SHOW INDEX FROM Students_InnoDB;

-- Do not execute this statement; ordinary InnoDB indexes
-- do not support explicit USING HASH:
-- CREATE INDEX idx_hash_name
-- ON Students_InnoDB(Student_Name) USING HASH;
\n\n-- ========================================================================\n-- 08_drop_index_and_compare.sql\n-- ========================================================================\n-- Experiment 8: Drop an index and compare
USE IndexHashLab;

DROP INDEX idx_student_city
ON Students_NoIndex;

EXPLAIN
SELECT *
FROM Students_NoIndex
WHERE City = 'Jaipur';
\n