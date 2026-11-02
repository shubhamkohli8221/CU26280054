-- Experiment 4: Run this pattern in BOTH sessions.
-- Ensure both transactions lock account 1 before account 2.
USE ConcurrencyLab;
START TRANSACTION;

SELECT * FROM Accounts
WHERE Account_ID = 1
FOR UPDATE;

SELECT * FROM Accounts
WHERE Account_ID = 2
FOR UPDATE;

-- Perform the required updates here.
-- Use the same account-lock order in both sessions.
COMMIT;
