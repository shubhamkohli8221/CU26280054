# DBMS Lab: Locking, Deadlocks, 2PL and Timestamp Ordering

MySQL practical files and practice questions extracted from the supplied lab sheet.

## Requirements
- MySQL 8.0
- MySQL Workbench or MySQL Shell
- Two separate MySQL sessions for concurrency experiments

## Folder structure
- `sql/01_setup.sql` — create the `ConcurrencyLab` database and sample accounts.
- `sql/02_row_lock_session_A.sql` and `sql/03_row_lock_session_B.sql` — demonstrate a row lock.
- `sql/04_deadlock_session_A.sql` and `sql/05_deadlock_session_B.sql` — demonstrate a deadlock.
- `sql/06_consistent_lock_order.sql` — lock rows in the same order.
- `sql/07_isolation_session_A.sql` and `sql/08_isolation_session_B.sql` — observe READ COMMITTED behavior.
- `sql/09_innodb_deadlock_status.sql` — inspect InnoDB status.
- `practice/2pl_schedule.md` — 2PL schedule exercises.
- `practice/timestamp_ordering.md` — timestamp-ordering simulation.
- `practice/lab_questions.md` — lab questions and observation checklist.

## How to run
1. Open MySQL Workbench.
2. Run `sql/01_setup.sql` once.
3. For row-lock, deadlock, and isolation experiments, open **two connections** to the same MySQL server and run the Session A and Session B files in the order described in each file.
4. Interleave statements between sessions as instructed. Do not run both sessions as one sequential batch.
5. Commit or roll back open transactions before starting another experiment.

## Important notes
- InnoDB manages locks and deadlocks itself. A deadlock victim is typically rolled back by InnoDB; applications should be ready to retry.
- The timestamp-ordering section is a **manual schedule simulation**. MySQL does not provide an ordinary SQL command to enable textbook timestamp ordering.
- The 2PL schedule files are also schedule-analysis exercises, not commands that switch MySQL into textbook 2PL mode.
- Results can vary with MySQL version, isolation level, query plan, and timing.

## Reset sample data
Run `sql/01_setup.sql` again to recreate the sample table and rows.
