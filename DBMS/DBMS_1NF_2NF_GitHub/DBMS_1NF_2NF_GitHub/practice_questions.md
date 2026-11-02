# Practice Questions — DBMS Normalization (1NF and 2NF)

Based on the supplied lab sheet.

1. Create the unnormalized table and identify its data problems.
2. Convert the sample table into 1NF.
3. Identify the composite primary key in 1NF.
4. Identify all partial dependencies.
5. Create the three 2NF tables.
6. Explain the role of primary and foreign keys.
7. Add a new student without an enrollment.
8. Add a new course without an enrollment.
9. Change the faculty assigned to Java.
10. Use JOIN to retrieve all enrollment details.

## Concepts to revise

- **UNF:** The original table contains multiple values in some cells.
- **1NF:** Each cell contains one atomic value and there are no repeating groups.
- **Composite key in 1NF:** `(Student_ID, Course_ID)`.
- **Partial dependencies:** `Student_ID → Student_Name`, `Course_ID → Course_Name`, and `Course_ID → Faculty_Name`.
- **2NF decomposition:** `Students`, `Courses`, and `Enrollments`.

## Notes

- The lab sheet assumes each course has one assigned faculty member.
- Run the SQL script from top to bottom in one MySQL session where possible.
- The final update and delete statements change the sample data. Re-run the script in a fresh database if you want to repeat the lab from the beginning.
