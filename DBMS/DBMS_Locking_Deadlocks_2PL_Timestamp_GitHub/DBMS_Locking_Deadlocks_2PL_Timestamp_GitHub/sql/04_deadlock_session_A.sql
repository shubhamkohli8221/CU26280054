-- Experiment 3: Session A
USE ConcurrencyLab;
START TRANSACTION;

-- Lock account 1 first.
UPDATE Accounts
SET Balance = Balance - 10
WHERE Account_ID = 1;

-- After Session B has locked account 2, request account 2.
-- This statement waits for Session B:
UPDATE Accounts
SET Balance = Balance + 10
WHERE Account_ID = 2;

-- InnoDB typically detects the circular wait and rolls back one victim.
-- If this transaction remains open, COMMIT or ROLLBACK explicitly.
