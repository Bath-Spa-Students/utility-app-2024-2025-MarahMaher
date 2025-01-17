# Simple Vending Machine in Python

def vending_machine():
    # Items available in the vending machine
    products = {
        "1": {"name": "Doritos", "price": 4.50},
        "2": {"name": "Lays", "price": 2.00},
        "3": {"name": "Cheetos", "price": 5.00},
        "4": {"name": "Water", "price": 1.00},
        "5": {"name": "Cola", "price": 3.00},
        "6": {"name": "jucie", "price": 5.00}
    }

    print("Welcome to the Vending Machine!\n")
    print("Available products:")
    for key, products in products.items():
        print(f"{key}. {products['name']} - aed{products['price']:.2f}")

    # User selects an item
    choice = input("\nEnter the number of the item you want to buy: ")

    if choice not in products:
        print("Invalid selection. Please try again.")
        return

    selected_products = products[choice]
    print(f"You selected {selected_products['name']} which costs ${selected_products['price']:.2f}")

    # User inserts money
    try:
        money_inserted = float(input("\nInsert money: aed"))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if money_inserted < selected_products['price']:
        print("Insufficient funds. Transaction canceled.")
        return

    # Calculate change
    change = money_inserted - selected_products['price']

    print(f"\nDispensing {selected_products['name']}...")
    if change > 0:
        print(f"Here is your change: aed{change:.2f}")

    print("Thank you for using the vending machine!")

# Run the vending machine program
if __name__ == "__main__":
    vending_machine()
