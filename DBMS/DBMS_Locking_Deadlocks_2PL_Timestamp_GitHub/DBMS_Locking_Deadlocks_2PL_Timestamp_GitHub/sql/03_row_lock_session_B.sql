-- Experiment 2: Session B
USE ConcurrencyLab;
START TRANSACTION;

UPDATE Accounts
SET Balance = Balance + 50
WHERE Account_ID = 1;

-- This UPDATE normally waits while Session A holds the row lock.
-- After Session A commits and this UPDATE completes, execute:
COMMIT;

SELECT * FROM Accounts WHERE Account_ID = 1;
