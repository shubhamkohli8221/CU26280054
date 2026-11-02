# Menu-driven CRUD application for an in-memory list of books.
books = []
def add():
    books.append({"id": input("Book ID: ").strip(),
                  "title": input("Title: ").strip(),
                  "author": input("Author: ").strip()})
    print("Book added.")
def view():
    for book in books: print(book)
    if not books: print("No books.")
def update():
    book_id = input("Book ID: ").strip()
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        book["title"] = input("New title: ").strip()
        book["author"] = input("New author: ").strip()
        print("Book updated.")
    else: print("Book not found.")
def delete():
    book_id = input("Book ID: ").strip()
    old = len(books)
    books[:] = [b for b in books if b["id"] != book_id]
    print("Book deleted." if len(books) < old else "Book not found.")
while True:
    choice = input("\\n1.Add 2.View 3.Update 4.Delete 5.Exit: ").strip()
    if choice == "1": add()
    elif choice == "2": view()
    elif choice == "3": update()
    elif choice == "4": delete()
    elif choice == "5": break
    else: print("Invalid choice.")
