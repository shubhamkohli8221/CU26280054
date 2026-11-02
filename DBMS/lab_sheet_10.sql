-- =====================================================
-- DBMS LAB SHEET 10
-- HOSPITAL MEDICINE MANAGEMENT SYSTEM
-- Database: HospitalDB
-- SQL Dialect: MySQL 8.0+
-- =====================================================


-- Q1
-- Create HospitalDB database and medicines table.

CREATE DATABASE IF NOT EXISTS HospitalDB;

USE HospitalDB;

CREATE TABLE IF NOT EXISTS medicines (
    medicine_id INT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    manufacturer VARCHAR(150) NOT NULL,
    supplier_id INT NULL
);

-- Insert at least 8 medicine records.

INSERT INTO medicines
(medicine_id, name, category, price, stock, manufacturer)
VALUES
(301, 'Paracetamol', 'Analgesic', 25.00, 100, 'ABC Pharma'),
(302, 'Amoxicillin', 'Antibiotic', 85.00, 45, 'HealthCare Labs'),
(303, 'Cetirizine', 'Antihistamine', 18.00, 25, 'MediLife'),
(304, 'Ibuprofen', 'Analgesic', 60.00, 70, 'ABC Pharma'),
(305, 'Azithromycin', 'Antibiotic', 120.00, 18, 'Wellness Pharma'),
(306, 'Omeprazole', 'Antacid', 95.00, 12, 'HealthCare Labs'),
(307, 'Vitamin C', 'Supplement', 45.00, 80, 'NutriMed'),
(308, 'Metformin', 'Antidiabetic', 55.00, 28, 'MediLife');

-- Display all medicine records.

SELECT * FROM medicines;



-- Q2
-- HTML medicine entry form is not an SQL task.
-- The form should contain:
-- Medicine ID, Medicine Name, Category,
-- Price, Stock and Manufacturer.
--
-- The form submission should execute an INSERT query.

INSERT INTO medicines
(medicine_id, name, category, price, stock, manufacturer)
VALUES
(309, 'Dolo 650', 'Analgesic', 32.00, 60, 'Micro Labs');



-- Q3
-- CSS styling is not an SQL task.
-- The medicines table created in Q1 provides
-- the database structure for the medicine entry form.



-- Q4
-- Flask and PyMongo connection code is not SQL.
-- In this SQL version, connect the application
-- to the HospitalDB MySQL database.

USE HospitalDB;

-- Verify database connection.

SELECT DATABASE() AS connected_database;

-- Display available tables.

SHOW TABLES;



-- Q5
-- Insert a medicine submitted through the form.

INSERT INTO medicines
(medicine_id, name, category, price, stock, manufacturer)
VALUES
(310, 'Cough Syrup', 'Cough Suppressant', 75.00, 35, 'CarePlus Pharma');

-- Verify inserted medicine.

SELECT *
FROM medicines
WHERE medicine_id = 310;



-- Q6
-- Retrieve all medicine records.

SELECT
    medicine_id,
    name,
    category,
    price,
    stock,
    manufacturer
FROM medicines
ORDER BY medicine_id;



-- Q7
-- Search medicine using Medicine ID.

SELECT *
FROM medicines
WHERE medicine_id = 302;


-- Search medicine using Medicine Name.

SELECT *
FROM medicines
WHERE name = 'Cetirizine';


-- Search medicine using partial name.

SELECT *
FROM medicines
WHERE name LIKE '%para%';

-- If no record is returned,
-- the application should display:
-- Medicine not found.



-- Q8
-- Update stock of a medicine using Medicine ID.

UPDATE medicines
SET stock = 90
WHERE medicine_id = 302;

-- Display updated medicine information.

SELECT *
FROM medicines
WHERE medicine_id = 302;



-- Q9
-- Delete medicine using Medicine ID.

DELETE FROM medicines
WHERE medicine_id = 310;

-- Verify deletion.

SELECT *
FROM medicines
WHERE medicine_id = 310;



-- Q10
-- (a) Display medicines belonging to a particular category.

SELECT *
FROM medicines
WHERE category = 'Analgesic';


-- (b) Display medicines costing more than ₹50.

SELECT *
FROM medicines
WHERE price > 50;


-- (c) Display medicines costing less than ₹100.

SELECT *
FROM medicines
WHERE price < 100;


-- (d) Display medicines having stock less than 30.

SELECT *
FROM medicines
WHERE stock < 30;


-- (e) Display medicines manufactured by a particular manufacturer.

SELECT *
FROM medicines
WHERE manufacturer = 'ABC Pharma';


-- (f) Sort medicines according to price.

SELECT *
FROM medicines
ORDER BY price ASC;


-- (g) Sort medicines according to stock.

SELECT *
FROM medicines
ORDER BY stock ASC;



-- Q11
-- Store supplier information using a separate relational table.
-- This is the SQL equivalent of MongoDB embedded documents.

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    phone VARCHAR(25),
    city VARCHAR(100)
);

-- Insert at least 3 suppliers.

INSERT INTO suppliers
(supplier_id, name, phone, city)
VALUES
(1, 'Reliable Medical Supplies', '9876543210', 'Aligarh'),
(2, 'City Pharma Distributors', '9876501234', 'Delhi'),
(3, 'Health First Suppliers', '9123456780', 'Agra');

-- Link medicines with suppliers.

UPDATE medicines
SET supplier_id = 1
WHERE medicine_id = 301;

UPDATE medicines
SET supplier_id = 2
WHERE medicine_id = 302;

UPDATE medicines
SET supplier_id = 3
WHERE medicine_id = 303;

-- Create foreign key relationship.

ALTER TABLE medicines
ADD CONSTRAINT fk_medicines_supplier
FOREIGN KEY (supplier_id)
REFERENCES suppliers(supplier_id);

-- Retrieve medicine and supplier information.

SELECT
    m.medicine_id,
    m.name AS medicine_name,
    m.category,
    m.price,
    m.stock,
    m.manufacturer,
    s.name AS supplier_name,
    s.phone AS supplier_phone,
    s.city AS supplier_city
FROM medicines AS m
LEFT JOIN suppliers AS s
ON m.supplier_id = s.supplier_id;



-- Q12
-- Generate Medicine Inventory Report.


-- (a) Display total number of medicines.

SELECT COUNT(*) AS total_medicines
FROM medicines;


-- (b) Display total stock of all medicines.

SELECT SUM(stock) AS total_stock
FROM medicines;


-- (c) Display medicines having low stock.
-- Low stock means fewer than 30 units.

SELECT *
FROM medicines
WHERE stock < 30;


-- (d) Display the most expensive medicine.

SELECT *
FROM medicines
WHERE price = (
    SELECT MAX(price)
    FROM medicines
);


-- (e) Display the cheapest medicine.

SELECT *
FROM medicines
WHERE price = (
    SELECT MIN(price)
    FROM medicines
);


-- Complete Inventory Summary.

SELECT
    COUNT(*) AS total_medicines,
    SUM(stock) AS total_stock,
    SUM(
        CASE
            WHEN stock < 30 THEN 1
            ELSE 0
        END
    ) AS low_stock_medicine_count,
    MAX(price) AS highest_price,
    MIN(price) AS lowest_price
FROM medicines;



-- Q13
-- Complete Hospital Medicine Management System
-- Home, Add, View, Search, Update, Delete,
-- Low Stock and Inventory Report.


-- HOME: Display inventory overview.

SELECT
    COUNT(*) AS total_medicines,
    SUM(stock) AS total_stock
FROM medicines;


-- ADD MEDICINE.

INSERT INTO medicines
(medicine_id, name, category, price, stock, manufacturer)
VALUES
(311, 'Antacid Tablets', 'Antacid', 40.00, 50, 'CarePlus Pharma');


-- VIEW MEDICINES.

SELECT *
FROM medicines
ORDER BY medicine_id;


-- SEARCH MEDICINE BY ID OR NAME.

SELECT *
FROM medicines
WHERE medicine_id = 311
OR name LIKE '%Antacid Tablets%';


-- UPDATE MEDICINE STOCK.

UPDATE medicines
SET stock = 75
WHERE medicine_id = 311;


-- VERIFY UPDATED STOCK.

SELECT
    medicine_id,
    name,
    stock
FROM medicines
WHERE medicine_id = 311;


-- DELETE MEDICINE.

DELETE FROM medicines
WHERE medicine_id = 311;


-- LOW STOCK MEDICINES.

SELECT *
FROM medicines
WHERE stock < 30
ORDER BY stock ASC;


-- INVENTORY REPORT.

SELECT
    COUNT(*) AS total_medicines,
    SUM(stock) AS total_stock,
    SUM(
        CASE
            WHEN stock < 30 THEN 1
            ELSE 0
        END
    ) AS low_stock_count,
    MAX(price) AS most_expensive_price,
    MIN(price) AS cheapest_price
FROM medicines;