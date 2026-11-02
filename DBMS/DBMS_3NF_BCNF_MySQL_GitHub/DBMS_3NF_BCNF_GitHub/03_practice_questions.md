# Practice Questions — 3NF and BCNF

These are the ten questions from the supplied lab sheet, followed by concise
answer guidance. The practical SQL tasks are also available in
`02_practice_questions.sql`.

1. **Explain transitive dependency using Course_ID, Faculty_ID, and Faculty_Name.**  
   `Course_ID → Faculty_ID` and `Faculty_ID → Faculty_Name`. Therefore,
   `Faculty_Name` depends on `Course_ID` indirectly through `Faculty_ID`.

2. **Why is Faculty_Name moved to a separate table when converting the example to 3NF?**  
   A faculty name depends on `Faculty_ID`, not directly on the course. Keeping it
   in a separate Faculty table removes the transitive dependency and avoids
   repeated faculty details and update anomalies.

3. **Write the functional dependencies in the Courses_2NF table.**  
   `Course_ID → Course_Name, Faculty_ID` and `Faculty_ID → Faculty_Name`.

4. **Insert a new faculty member before assigning that person to a course.**  
   Use an `INSERT` into `Faculty` first. Example:
   ```sql
   INSERT INTO Faculty (Faculty_ID, Faculty_Name)
   VALUES ('F04', 'Mehta');
   ```

5. **Add a new course and assign it to an existing faculty member.**  
   Insert the course into `Courses_3NF`, using a `Faculty_ID` already present in
   `Faculty`. Example:
   ```sql
   INSERT INTO Courses_3NF (Course_ID, Course_Name, Faculty_ID)
   VALUES ('C05', 'Data Structures', 'F04');
   ```

6. **Update a faculty name and verify the result using JOIN.**  
   Update the row once in `Faculty`, then join `Courses_3NF` to `Faculty` to see
   the new name for all courses assigned to that faculty member. See the SQL
   script for a complete example.

7. **Define BCNF and explain why it is stricter than 3NF.**  
   BCNF requires every determinant in every non-trivial functional dependency
   to be a superkey. 3NF also permits a dependency when its dependent attribute
   is prime, so a 3NF relation can still violate BCNF.

8. **Identify the candidate keys in Student_Instructor_Subject.**  
   Under the functional dependencies in the lab sheet, the candidate keys are
   `(Student, Instructor)` and `(Student, Subject)`.

9. **Explain why Instructor → Subject violates BCNF in the given scenario.**  
   `Instructor` determines `Subject`, but `Instructor` alone is not a superkey
   because one instructor can be associated with multiple students. BCNF
   requires the determinant to be a superkey. The lab's stated 3NF condition is
   satisfied because `Subject` is a prime attribute.

10. **Create the BCNF decomposition and reconstruct the data using JOIN.**  
    Create `Instructor_Subject` with `Instructor` as its primary key and
    `Student_Instructor` with `(Student, Instructor)` as its composite primary
    key and `Instructor` as a foreign key. Join them on `Instructor` to
    reconstruct the student, instructor, and subject rows.

## Normal-form comparison

| Normal form | Main rule |
|---|---|
| 2NF | 1NF plus no partial dependency on a candidate key |
| 3NF | For every functional dependency `X → A`, `X` is a superkey or `A` is prime |
| BCNF | For every non-trivial functional dependency `X → Y`, `X` is a superkey |

BCNF is stricter than 3NF. A relation in BCNF is also in 3NF, but a relation
in 3NF is not always in BCNF.
