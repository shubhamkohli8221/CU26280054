# Store and manage products using a dictionary keyed by product ID.
products = {}
def add():
    pid = input("Product ID: ").strip()
    products[pid] = {"name": input("Name: ").strip(),
                     "price": float(input("Price: ")),
                     "quantity": int(input("Quantity: "))}
    print("Product saved.")
def view():
    for pid, product in products.items(): print(pid, product)
    if not products: print("No products.")
def update():
    pid = input("Product ID: ").strip()
    if pid in products:
        products[pid]["price"] = float(input("New price: "))
        products[pid]["quantity"] = int(input("New quantity: "))
        print("Product updated.")
    else: print("Product not found.")
def delete():
    pid = input("Product ID: ").strip()
    print("Deleted." if products.pop(pid, None) is not None else "Product not found.")
try:
    while True:
        choice = input("\\n1.Add 2.View 3.Update 4.Delete 5.Exit: ").strip()
        if choice == "1": add()
        elif choice == "2": view()
        elif choice == "3": update()
        elif choice == "4": delete()
        elif choice == "5": break
        else: print("Invalid choice.")
except ValueError:
    print("Price and quantity must be numeric.")
