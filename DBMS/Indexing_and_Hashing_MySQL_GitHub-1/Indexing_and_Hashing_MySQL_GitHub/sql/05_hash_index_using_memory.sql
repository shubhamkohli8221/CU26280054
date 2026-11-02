-- Experiment 5: Create a hash index using MEMORY
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
