# 19. Delete students with marks below 40.
import sqlite3
try:
    if input("Delete students scoring below 40? Type YES: ") == "YES":
        with sqlite3.connect("student_db.db") as con:
            cur = con.execute("DELETE FROM students WHERE marks < ?", (40,))
        print("Records deleted:", cur.rowcount)
    else: print("Cancelled.")
except sqlite3.Error as e:
    print("Database error:", e)
