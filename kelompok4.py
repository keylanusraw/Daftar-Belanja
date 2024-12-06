class ShoppingItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (x{self.quantity}): ${self.price:.2f}" 


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = ShoppingItem(name, quantity, price)
        self.items.append(item)
        print(f"Added: {item}")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print("Item not found!")

    def display_list(self):
        if not self.items:
            print("Shopping list is empty.")
        else:
            print("Shopping List:")
            for item in self.items:
                print(f" - {item}")


def main():
    shopping_list = ShoppingList()
    while True:
        print("\n==== Shopping List Menu ====")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display shopping list")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per unit: "))
                shopping_list.add_item(name, quantity, price)
            except ValueError:
                print("Invalid input! Quantity and price must be numbers.")
        elif choice == "2":
            name = input("Enter the name of the item to remove: ")
            shopping_list.remove_item(name)
        elif choice == "3":
            shopping_list.display_list()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")


if __name__ == "__main__":
    main()