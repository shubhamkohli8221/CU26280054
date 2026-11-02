-- Experiment 1: Create a table without an index
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
