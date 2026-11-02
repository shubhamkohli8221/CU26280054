-- Experiment 3: Session B
USE ConcurrencyLab;
START TRANSACTION;

-- Lock account 2 first.
UPDATE Accounts
SET Balance = Balance - 20
WHERE Account_ID = 2;

-- After Session A is waiting for account 2, request account 1.
-- This creates circular wait:
UPDATE Accounts
SET Balance = Balance + 20
WHERE Account_ID = 1;

-- InnoDB typically detects a deadlock and rolls back one transaction.
-- Inspect the error; explicitly COMMIT or ROLLBACK if still open.
