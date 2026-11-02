-- Practical exercises from the lab sheet.
-- Run 01_full_lab.sql first.
USE Normalization3NF_BCNF;

-- QUESTION 4: Insert a faculty member before assigning that person to a course.
INSERT INTO Faculty (Faculty_ID, Faculty_Name)
VALUES ('F04', 'Mehta');

SELECT * FROM Faculty WHERE Faculty_ID = 'F04';

-- QUESTION 5: Add a new course and assign it to an existing faculty member.
INSERT INTO Courses_3NF (Course_ID, Course_Name, Faculty_ID)
VALUES ('C05', 'Data Structures', 'F04');

SELECT c.Course_ID, c.Course_Name, f.Faculty_Name
FROM Courses_3NF AS c
JOIN Faculty AS f ON c.Faculty_ID = f.Faculty_ID
WHERE c.Course_ID = 'C05';

-- QUESTION 6: Update a faculty name and verify the result using JOIN.
UPDATE Faculty
SET Faculty_Name = 'Dr Mehta'
WHERE Faculty_ID = 'F04';

SELECT c.Course_ID, c.Course_Name, f.Faculty_Name
FROM Courses_3NF AS c
JOIN Faculty AS f ON c.Faculty_ID = f.Faculty_ID
WHERE f.Faculty_ID = 'F04';

-- QUESTION 10: Reconstruct the BCNF-decomposed data using JOIN.
SELECT
    si.Student,
    si.Instructor,
    ins.Subject
FROM Student_Instructor AS si
JOIN Instructor_Subject AS ins
    ON si.Instructor = ins.Instructor
ORDER BY si.Student, si.Instructor;

-- EXTRA PRACTICE:
-- 1. Display all courses with their faculty names.
SELECT c.Course_ID, c.Course_Name, f.Faculty_Name
FROM Courses_3NF AS c
INNER JOIN Faculty AS f ON c.Faculty_ID = f.Faculty_ID;

-- 2. Count how many courses are assigned to each faculty member.
SELECT f.Faculty_ID, f.Faculty_Name, COUNT(c.Course_ID) AS Total_Courses
FROM Faculty AS f
LEFT JOIN Courses_3NF AS c ON f.Faculty_ID = c.Faculty_ID
GROUP BY f.Faculty_ID, f.Faculty_Name;

-- 3. Find instructors who teach DBMS.
SELECT Instructor
FROM Instructor_Subject
WHERE Subject = 'DBMS';
