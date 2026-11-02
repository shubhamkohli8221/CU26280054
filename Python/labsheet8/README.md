# MCA101P — Lab Sheet 08: Database Management using Python

These 30 Python programs are based on the questions in `MCA101P-AS11.pdf`.

## Database used
All programs use **SQLite** and the database file `student_db.db`. SQLite is included with Python 3, so no external package is required.

## How to run
1. Install Python 3.
2. Open this folder in VS Code.
3. Run programs from the terminal, for example:
   `python 03_create_students_table.py`
4. Run `03_create_students_table.py` before programs that use the `students` table.
5. Run `21_create_courses_table.py` before programs 22 and 23.
6. Program 27 expects `students_import.csv` with rows in `name,age,marks` format and no header.
7. Run the menu-driven program with `python 30_menu_driven_student_management.py`.

## Notes
- Every script includes comments and basic exception handling.
- Parameterized SQL queries (`?`) are used for user-provided values.
- `with sqlite3.connect(...)` safely commits successful changes and closes the connection.
- SQLite creates `student_db.db` automatically when first opened.
- SQLite does not support `TRUNCATE TABLE`; program 20 uses `DELETE FROM students` to remove rows while preserving the table structure.
- Programs 6, 18, 19, and 20 change or delete data, so read the confirmation prompt carefully.
- For the INNER/LEFT JOIN examples, the relationship matches `students.id` with `courses.course_id`, because the assignment does not specify a linking column.
