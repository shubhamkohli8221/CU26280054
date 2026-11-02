-- Experiment 5: Session A
USE ConcurrencyLab;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;

SELECT * FROM Accounts WHERE Account_ID = 1;
UPDATE Accounts
SET Balance = Balance + 100
WHERE Account_ID = 1;

-- Keep the transaction open while Session B performs a normal SELECT.
-- Then execute:
COMMIT;
