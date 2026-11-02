# DBMS Lab: 3NF and BCNF (MySQL)

This repository contains the MySQL programs and practice material from the supplied
**DBMS Lab Sheet: Third Normal Form (3NF) and Boyce–Codd Normal Form (BCNF)**.

## Requirements
- MySQL 8.0 or later
- MySQL Workbench or MySQL Shell

## Files
- `01_full_lab.sql` — all seven lab programs in execution order.
- `02_practice_questions.sql` — practical SQL exercises and sample solutions.
- `03_practice_questions.md` — all ten practice questions with concise answer guidance.

## How to run
1. Open MySQL Workbench (or MySQL Shell).
2. Open `01_full_lab.sql`.
3. Execute the complete script from top to bottom.
4. Open `02_practice_questions.sql` and run the exercises after the lab script.
5. Read `03_practice_questions.md` for the theory questions and explanations.

The scripts create and use a separate database named `Normalization3NF_BCNF`.
The lab script drops its own tables first so it can be rerun safely. It does not
drop the database itself.

## Topics covered
- Transitive functional dependencies
- Conversion from a 2NF-style course table to 3NF
- Primary keys and foreign keys
- JOIN queries
- 3NF versus BCNF
- BCNF decomposition and reconstruction

## GitHub upload
Create a new GitHub repository, then upload these extracted files (or upload this
ZIP directly if you prefer to keep the ZIP as an archive). A useful repository
name is `DBMS-3NF-BCNF-MySQL-Lab`.
