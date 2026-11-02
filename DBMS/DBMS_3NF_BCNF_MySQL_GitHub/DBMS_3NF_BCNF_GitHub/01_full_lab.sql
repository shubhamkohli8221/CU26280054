-- DBMS Lab Sheet: Third Normal Form (3NF) and BCNF
-- MySQL 8.0+
-- Programs 1 to 7, in the order given in the lab sheet.

CREATE DATABASE IF NOT EXISTS Normalization3NF_BCNF;
USE Normalization3NF_BCNF;

-- Remove old lab tables so this script can be executed again.
DROP TABLE IF EXISTS Student_Instructor;
DROP TABLE IF EXISTS Instructor_Subject;
DROP TABLE IF EXISTS Student_Instructor_Subject;
DROP TABLE IF EXISTS Courses_3NF;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Courses_2NF;

-- =========================================================
-- PROGRAM 1: Create database and demonstrate transitive dependency
-- =========================================================
CREATE TABLE Courses_2NF (
    Course_ID VARCHAR(10) PRIMARY KEY,
    Course_Name VARCHAR(50) NOT NULL,
    Faculty_ID VARCHAR(10) NOT NULL,
    Faculty_Name VARCHAR(50) NOT NULL
);

INSERT INTO Courses_2NF VALUES
('C01', 'DBMS', 'F01', 'Sharma'),
('C02', 'Java', 'F02', 'Verma'),
('C03', 'Python', 'F03', 'Khan'),
('C04', 'SQL', 'F01', 'Sharma');

SELECT * FROM Courses_2NF;

-- Observation: F01 / Sharma is repeated for more than one course.

-- =========================================================
-- PROGRAM 2: Convert the design into 3NF tables
-- =========================================================
CREATE TABLE Faculty (
    Faculty_ID VARCHAR(10) PRIMARY KEY,
    Faculty_Name VARCHAR(50) NOT NULL
);

CREATE TABLE Courses_3NF (
    Course_ID VARCHAR(10) PRIMARY KEY,
    Course_Name VARCHAR(50) NOT NULL,
    Faculty_ID VARCHAR(10) NOT NULL,
    FOREIGN KEY (Faculty_ID) REFERENCES Faculty(Faculty_ID)
);

INSERT INTO Faculty VALUES
('F01', 'Sharma'),
('F02', 'Verma'),
('F03', 'Khan');

INSERT INTO Courses_3NF VALUES
('C01', 'DBMS', 'F01'),
('C02', 'Java', 'F02'),
('C03', 'Python', 'F03'),
('C04', 'SQL', 'F01');

SELECT * FROM Faculty;
SELECT * FROM Courses_3NF;

-- =========================================================
-- PROGRAM 3: Display course and faculty details using JOIN
-- =========================================================
SELECT
    c.Course_ID,
    c.Course_Name,
    f.Faculty_ID,
    f.Faculty_Name
FROM Courses_3NF AS c
JOIN Faculty AS f
    ON c.Faculty_ID = f.Faculty_ID
ORDER BY c.Course_ID;

-- =========================================================
-- PROGRAM 4: Test an update in 3NF
-- =========================================================
UPDATE Faculty
SET Faculty_Name = 'Dr Sharma'
WHERE Faculty_ID = 'F01';

SELECT * FROM Faculty WHERE Faculty_ID = 'F01';

SELECT c.Course_ID, c.Course_Name, f.Faculty_Name
FROM Courses_3NF AS c
JOIN Faculty AS f
    ON c.Faculty_ID = f.Faculty_ID
WHERE f.Faculty_ID = 'F01';

-- =========================================================
-- PROGRAM 5: Create the 3NF-but-not-BCNF relation
-- =========================================================
CREATE TABLE Student_Instructor_Subject (
    Student VARCHAR(30),
    Instructor VARCHAR(10),
    Subject VARCHAR(30),
    PRIMARY KEY (Student, Instructor),
    UNIQUE (Student, Subject)
);

INSERT INTO Student_Instructor_Subject VALUES
('Asha', 'I01', 'DBMS'),
('Ravi', 'I01', 'DBMS'),
('Asha', 'I02', 'Java'),
('Mohan', 'I02', 'Java');

SELECT * FROM Student_Instructor_Subject;

-- Note: Instructor -> Subject is a business rule in this example.
-- The UNIQUE constraints above do not independently enforce that rule.

-- =========================================================
-- PROGRAM 6: Decompose the relation into BCNF
-- =========================================================
CREATE TABLE Instructor_Subject (
    Instructor VARCHAR(10) PRIMARY KEY,
    Subject VARCHAR(30) NOT NULL
);

CREATE TABLE Student_Instructor (
    Student VARCHAR(30),
    Instructor VARCHAR(10),
    PRIMARY KEY (Student, Instructor),
    FOREIGN KEY (Instructor) REFERENCES Instructor_Subject(Instructor)
);

INSERT INTO Instructor_Subject VALUES
('I01', 'DBMS'),
('I02', 'Java');

INSERT INTO Student_Instructor VALUES
('Asha', 'I01'),
('Ravi', 'I01'),
('Asha', 'I02'),
('Mohan', 'I02');

SELECT * FROM Instructor_Subject;
SELECT * FROM Student_Instructor;

-- =========================================================
-- PROGRAM 7: Reconstruct the original information
-- =========================================================
SELECT
    si.Student,
    si.Instructor,
    ins.Subject
FROM Student_Instructor AS si
JOIN Instructor_Subject AS ins
    ON si.Instructor = ins.Instructor
ORDER BY si.Student, si.Instructor;
