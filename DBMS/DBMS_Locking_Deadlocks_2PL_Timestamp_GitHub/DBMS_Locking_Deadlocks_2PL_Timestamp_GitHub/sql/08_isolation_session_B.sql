-- Experiment 5: Session B
USE ConcurrencyLab;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;

SELECT * FROM Accounts WHERE Account_ID = 1;
-- A normal consistent read generally sees the last committed value,
-- not Session A's uncommitted update.

COMMIT;

-- After Session A commits, run a new SELECT:
SELECT * FROM Accounts WHERE Account_ID = 1;
