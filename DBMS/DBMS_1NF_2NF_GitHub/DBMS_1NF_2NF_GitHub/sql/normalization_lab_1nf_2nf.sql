-- DBMS Lab Sheet: 1NF and 2NF Using MySQL
-- Run this script in MySQL Workbench or MySQL Shell.
-- Source: supplied DBMS Lab Sheet 1NF_2NF_MySQL document.

CREATE DATABASE IF NOT EXISTS NormalizationLab;
USE NormalizationLab;

-- PROGRAM 1: Create the unnormalized table (UNF)
CREATE TABLE Student_Course_UNF (
    Student_ID INT,
    Student_Name VARCHAR(50),
    Courses VARCHAR(100),
    Faculty VARCHAR(100)
);

INSERT INTO Student_Course_UNF
VALUES
    (101, 'Ravi', 'DBMS, Java', 'Sharma, Verma'),
    (102, 'Priya', 'DBMS', 'Sharma'),
    (103, 'Aman', 'Java, Python', 'Verma, Khan');

SELECT * FROM Student_Course_UNF;

-- PROGRAM 2: Create the First Normal Form (1NF) table
CREATE TABLE Student_Course_1NF (
    Student_ID INT,
    Student_Name VARCHAR(50),
    Course_ID VARCHAR(10),
    Course_Name VARCHAR(50),
    Faculty_Name VARCHAR(50),
    PRIMARY KEY (Student_ID, Course_ID)
);

INSERT INTO Student_Course_1NF
VALUES
    (101, 'Ravi', 'C01', 'DBMS', 'Sharma'),
    (101, 'Ravi', 'C02', 'Java', 'Verma'),
    (102, 'Priya', 'C01', 'DBMS', 'Sharma'),
    (103, 'Aman', 'C02', 'Java', 'Verma'),
    (103, 'Aman', 'C03', 'Python', 'Khan');

SELECT * FROM Student_Course_1NF;

-- PROGRAM 3: Create the Second Normal Form (2NF) tables
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(50) NOT NULL
);

CREATE TABLE Courses (
    Course_ID VARCHAR(10) PRIMARY KEY,
    Course_Name VARCHAR(50) NOT NULL,
    Faculty_Name VARCHAR(50) NOT NULL
);

CREATE TABLE Enrollments (
    Student_ID INT,
    Course_ID VARCHAR(10),
    PRIMARY KEY (Student_ID, Course_ID),
    FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
);

-- PROGRAM 4: Insert data into the 2NF tables
INSERT INTO Students VALUES
    (101, 'Ravi'),
    (102, 'Priya'),
    (103, 'Aman');

INSERT INTO Courses VALUES
    ('C01', 'DBMS', 'Sharma'),
    ('C02', 'Java', 'Verma'),
    ('C03', 'Python', 'Khan');

INSERT INTO Enrollments VALUES
    (101, 'C01'),
    (101, 'C02'),
    (102, 'C01'),
    (103, 'C02'),
    (103, 'C03');

-- PROGRAM 5: Display all 2NF tables
SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Enrollments;

-- PROGRAM 6: Retrieve complete enrollment details using JOIN
SELECT
    s.Student_ID,
    s.Student_Name,
    c.Course_ID,
    c.Course_Name,
    c.Faculty_Name
FROM Students AS s
JOIN Enrollments AS e
    ON s.Student_ID = e.Student_ID
JOIN Courses AS c
    ON e.Course_ID = c.Course_ID
ORDER BY s.Student_ID, c.Course_ID;

-- PROGRAM 7: Test independent insertion
-- Add a student who has not enrolled in any course.
INSERT INTO Students VALUES (104, 'Neha');
SELECT * FROM Students;

-- Add a course before any student enrolls in it.
INSERT INTO Courses VALUES ('C04', 'Python Lab', 'Mehta');
SELECT * FROM Courses;

-- PROGRAM 8: Test an update
-- Change the faculty assigned to DBMS.
UPDATE Courses
SET Faculty_Name = 'Mehta'
WHERE Course_ID = 'C01';

SELECT * FROM Courses
WHERE Course_ID = 'C01';

-- PROGRAM 9: Test deletion
-- Delete Ravi's DBMS enrollment; student and course records should remain.
DELETE FROM Enrollments
WHERE Student_ID = 101
  AND Course_ID = 'C01';

SELECT * FROM Enrollments;
SELECT * FROM Students WHERE Student_ID = 101;
SELECT * FROM Courses WHERE Course_ID = 'C01';
