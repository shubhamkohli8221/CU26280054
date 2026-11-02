-- =====================================================
-- DBMS LAB SHEET 9
-- STUDENT RECORD MANAGEMENT SYSTEM
-- Database: CollegeDB
-- SQL Dialect: MySQL 8.0+
-- =====================================================


-- Q1
-- Environment setup:
-- Install MySQL Server and MySQL Workbench.
-- Connect to the MySQL server using MySQL Workbench.
-- Python, Flask, PyMongo and MongoDB installation
-- are not SQL operations.


-- Q2
-- Create CollegeDB database and students table.
CREATE DATABASE IF NOT EXISTS CollegeDB;

USE CollegeDB;

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(20),
    department VARCHAR(100) NOT NULL,
    marks DECIMAL(5,2) NOT NULL
);

-- Insert at least 5 student records.
INSERT INTO students
(student_id, name, age, gender, department, marks)
VALUES
(101, 'Aarav Sharma', 21, 'Male', 'Computer Science', 88.50),
(102, 'Diya Verma', 20, 'Female', 'Mathematics', 76.00),
(103, 'Rohan Singh', 22, 'Male', 'Computer Science', 92.00),
(104, 'Ananya Gupta', 19, 'Female', 'Physics', 67.50),
(105, 'Kabir Khan', 23, 'Male', 'Commerce', 54.00);

-- Display all student records.
SELECT * FROM students;



-- Q3
-- HTML student registration form is not an SQL task.
-- The form should contain:
-- Student ID, Student Name, Age, Gender,
-- Department and Marks.
--
-- The form submission should execute an INSERT query.
-- Example database operation:

INSERT INTO students
(student_id, name, age, gender, department, marks)
VALUES
(106, 'Meera Joshi', 21, 'Female', 'Computer Science', 81.00);



-- Q4
-- CSS styling is not an SQL task.
-- The students table created in Q2 provides
-- the database structure for the registration form.



-- Q5
-- Flask and PyMongo connection code is not SQL.
-- In this SQL version, connect the application
-- to the CollegeDB MySQL database.

USE CollegeDB;

-- Verify database connection:
SELECT DATABASE() AS connected_database;

-- Display available tables:
SHOW TABLES;



-- Q6
-- Insert student information submitted through the form.

INSERT INTO students
(student_id, name, age, gender, department, marks)
VALUES
(107, 'Ishita Patel', 20, 'Female', 'Biotechnology', 84.00);

-- Verify the newly inserted student.
SELECT *
FROM students
WHERE student_id = 107;



-- Q7
-- Retrieve all student records.

SELECT
    student_id,
    name,
    age,
    gender,
    department,
    marks
FROM students
ORDER BY student_id;



-- Q8
-- Search for a student using Student ID.

SELECT *
FROM students
WHERE student_id = 103;

-- If no record is returned,
-- the application should display:
-- Student not found.



-- Q9
-- Update student's Name, Age, Department and Marks.

UPDATE students
SET
    name = 'Rohan Kumar',
    age = 23,
    department = 'Data Science',
    marks = 95.00
WHERE student_id = 103;

-- Verify the updated student record.

SELECT *
FROM students
WHERE student_id = 103;



-- Q10
-- Delete a student using Student ID.

DELETE FROM students
WHERE student_id = 107;

-- Verify deletion.

SELECT *
FROM students
WHERE student_id = 107;



-- Q11
-- (a) Display students belonging to a particular department.

SELECT *
FROM students
WHERE department = 'Computer Science';


-- (b) Display students having marks greater than 75.

SELECT *
FROM students
WHERE marks > 75;


-- (c) Display students having marks between 50 and 80.

SELECT *
FROM students
WHERE marks BETWEEN 50 AND 80;


-- (d) Display students older than 20 years.

SELECT *
FROM students
WHERE age > 20;



-- Q12
-- Complete Student Record Management System
-- Add, View, Search, Update and Delete operations.


-- ADD STUDENT

INSERT INTO students
(student_id, name, age, gender, department, marks)
VALUES
(108, 'Neha Mishra', 22, 'Female', 'Computer Science', 89.00);


-- VIEW ALL STUDENTS

SELECT *
FROM students
ORDER BY student_id;


-- SEARCH STUDENT

SELECT *
FROM students
WHERE student_id = 108;


-- UPDATE STUDENT

UPDATE students
SET
    name = 'Neha Singh',
    age = 23,
    department = 'Information Technology',
    marks = 91.00
WHERE student_id = 108;


-- VERIFY UPDATED STUDENT

SELECT *
FROM students
WHERE student_id = 108;


-- DELETE STUDENT

DELETE FROM students
WHERE student_id = 108;


-- VERIFY DELETION

SELECT *
FROM students
WHERE student_id = 108;