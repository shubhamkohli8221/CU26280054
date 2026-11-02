-- Experiment 1: Set up account data
CREATE DATABASE IF NOT EXISTS ConcurrencyLab;
USE ConcurrencyLab;

DROP TABLE IF EXISTS Accounts;

CREATE TABLE Accounts (
    Account_ID INT PRIMARY KEY,
    Account_Name VARCHAR(40) NOT NULL,
    Balance DECIMAL(10,2) NOT NULL
) ENGINE = InnoDB;

INSERT INTO Accounts VALUES
(1, 'Asha', 1000.00),
(2, 'Ravi', 1000.00);

SELECT * FROM Accounts;
