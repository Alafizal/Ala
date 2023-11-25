import csv
from prettytable import PrettyTable

def load_menu():
    try:
        with open('Database.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            menu = list(reader)
        return menu
    except FileNotFoundError:
        print("Error: The 'bakery_menu.csv' file was not found.")
    except Exception as e:
        print(f"An error occurred while loading the menu: {e}")
    return []

def generate_receipt(order_details, menu):
    total_amount = 0
    receipt = []

    print("\n======= Receipt =======")
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total"))

    for item_id, quantity in order_details.items():
        item = menu[int(item_id) - 1]
        item_name = item['Cake Name']
        item_price = float(item['Price'])
        total_item_price = item_price * quantity

        total_amount += total_item_price

        receipt.append({
            'Item': item_name,
            'Quantity': quantity,
            'Price': item_price,
            'Total': total_item_price
        })

        print("{:<20} {:<10} ${:<10.2f} ${:<10.2f}".format(item_name, quantity, item_price, total_item_price))

    print("========================")
    print("Total Amount: ${:.2f}\n".format(total_amount))

    return receipt

def main():
    menu = load_menu()

    if not menu:
        print("Exiting program due to errors.")
        return

    order_details = {}

    while True:
        display_menu(menu)
        
        item_id = input("Enter the ID of the item you want to purchase (0 to finish): ")
        
        if item_id == '0':
            break

        if not item_id.isdigit() or int(item_id) <= 0 or int(item_id) > len(menu):
            print("Invalid item ID. Please enter a valid ID.")
            continue

        quantity = int(input("Enter the quantity: "))
        order_details[item_id] = quantity

    receipt = generate_receipt(order_details, menu)

    # You can save the receipt to a file or perform further actions based on your requirements
    # For example, writing the receipt to a CSV file:
    with open('user_receipt.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Item', 'Quantity', 'Price', 'Total']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(receipt)

if __name__ == "__main__":
    main()

