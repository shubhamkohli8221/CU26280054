-- Experiment 2: Session A
USE ConcurrencyLab;
START TRANSACTION;

SELECT * FROM Accounts
WHERE Account_ID = 1
FOR UPDATE;

UPDATE Accounts
SET Balance = Balance - 100
WHERE Account_ID = 1;

-- Keep this transaction open while Session B attempts its UPDATE.
-- After observing Session B waiting, execute:
COMMIT;
