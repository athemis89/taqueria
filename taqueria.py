import random
import os

# Initialise the menu. There should be at least five mains and three sides. The mains should be made of multiple ingredients.
menu = {
    "Baja Taco": {"price": 4.00, "ingredients": ["tortilla", "meat", "cheese", "salsa", "guacamole"]},
    "Burrito": {"price": 7.50, "ingredients": ["tortilla", "rice", "meat", "beans", "cheese", "salsa", "sour cream"]},
    "Bowl": {"price": 8.50, "ingredients": ["rice", "meat", "beans", "lettuce", "salsa", "guacamole"]},
    "Nachos": {"price": 11.00, "ingredients": ["chips", "meat", "beans", "cheese", "salsa", "guacamole", "sour cream"]},
    "Quesadilla": {"price": 8.50, "ingredients": ["tortilla", "meat", "cheese"]},
    "Super Burrito": {"price": 8.50, "ingredients": ["tortilla", "rice", "meat", "beans", "cheese", "salsa", "sour cream"]},
    "Super Quesadilla": {"price": 9.50, "ingredients": ["tortilla", "meat", "cheese", "salsa", "guacamole", "sour cream"]},
    "Taco": {"price": 3.00, "ingredients": ["tortilla", "shrimp", "cheese", "salsa"]},
    "Tortilla Salad": {"price": 8.00, "ingredients": ["lettuce", "meat", "beans", "cheese", "salsa", "guacamole", "sour cream"]}
}

sides = {
    "Salad": {"price": 2.00, "ingredients": ["lettuce", "tomatoes", "lemon"]},
    "Fries": {"price": 3.50, "ingredients": ["potatoes", "salt"]},
    "Guacamole": {"price": 4.00, "ingredients": ["guacamole", "onion", "lime", "salt"]}
}


def main():
    print(" ")
    option = input("Select an option (1. New Order, 2. Track Order): ")
    print(" ")

    if option == "1":
        new_order(menu, sides)
    elif option == "2":
        track_order()
    else:
        print("Invalid option. Please try again.")


def welcome():

    # context
    print("This is YummmyNet.")
    print("-------------------------")
    print("Welcome to the Taqueria!")
    print(" ")

    # get post code
    post_code = None
    while post_code is None or len(post_code) < 4:
        try:
            post_code = input("For delivery, please enter your postcode: ")
        except:
            return post_code

    # show them the menu
    print(" ")
    print("Main Menu")
    for item, details in menu.items():
        print(f"{item}: ${details['price']}")
    print(" ")
    print("Sides")
    for item, details in sides.items():
        print(f"{item}: ${details['price']}")
    print(" ")

    # tell them to write 'done' once they've finished their order
    print("Please write down what you'd like to order. Once you're done, just write 'done'.")
    print(" ")


def new_order(menu, sides):
    # welcome and have the user select an order for delivery from the items on the menu.
    welcome()
    order = place_order(menu, sides)

    if order:
        order_number = generate_order_number()
        print(f"\nOrder number: {order_number}")

        # print the order
        print(f"Your order: ")
        for entry in order:
            item = entry["item"]
            quantity = entry["quantity"]
            if quantity > 1:
                print(f" - {item} x {quantity}")
            else:
                print(f" -{item}")

        # print total cost
        total_cost = calculate_total_cost(order, menu, sides)
        print(f"Total: ${total_cost:.2f}")

        # print delivery time
        if total_cost <= 15:
            print("Delivery Time: 30 min")
        elif total_cost <= 35:
            print("Delivery Time: 45 min")
        else:
            print("Delivery Time: 60 min")
        print(" ")

        # ask them to confirm by giving their phone number.
        phone_number = None
        while phone_number is None or len(phone_number) < 10:
            try:
                phone_number = input("Enter your phone number to confirm: ")
            except:
                print("Thank you for your order!")
                return phone_number

        # generate receipt
        generate_receipt(order_number, order, menu, sides, total_cost)
        save_order(order_number, order, total_cost, phone_number)

        # open the receipt file for the client
        #os.system(f"open receipt-{order_number}.txt")


def place_order(menu, sides):

    # randomly select an ingredient to be sold out
    sold_out_ingredient = random.choice(["meat", "rice", "tortilla", "shrimp", "salsa", "beans", "cheese", "guacamole", "lettuce"])
    #print(sold_out_ingredient) #for testing purposes

    # initialise empty list for order
    order = []

    # mapping of similar foods
    similar_foods = {
        "Baja Taco": ["Taco", "Quesadilla"],
        "Burrito": ["Super Burrito", "Bowl"],
        "Bowl": ["Burrito", "Tortilla Salad"],
        "Nachos": ["Quesadilla", "Tortilla Salad"],
        "Quesadilla": ["Burrito", "Tortilla Salad"],
        "Super Burrito": ["Burrito", "Bowl"],
        "Super Quesadilla": ["Quesadilla", "Tortilla Salad"],
        "Taco": ["Burrito", "Baja Taco"],
        "Tortilla Salad": ["Burrito", "Nachos"],
        # can expand mappings as needed
    }

    # order
    while True:
        try:
            item = input("Item: ").lower()
            menu_items = [menu_item.title() for menu_item in menu.keys()] + [side.title() for side in sides.keys()]

            if item == "done":
                break

            while item.title() not in menu_items:
                print("Invalid item. Please choose an item from the menu.")
                item = input("Item: ").lower()

            # if the user selects an item with that ingredient mention that it is sold out and offer an alternative.
            if item.title() in menu and sold_out_ingredient in menu[item.title()]["ingredients"]:
                print(f"Sorry, the {sold_out_ingredient} is sold out. Please choose a different item.")
                alternatives = similar_foods.get(item.title(), [])
                filtered_alternatives = [alt for alt in alternatives if sold_out_ingredient not in menu[alt]["ingredients"]]
                if filtered_alternatives:
                    suggestion = ", ".join(filtered_alternatives)
                    print(f"Alternative suggestion: {suggestion}")
                else:
                    not_similar_alternatives = [menu_item.title() for menu_item in menu if sold_out_ingredient not in menu[menu_item]["ingredients"]]
                    suggestion = ", ".join(not_similar_alternatives)
                    print(f"No similar alternatives available. You may consider: {suggestion}")

            elif item.title() in sides and sold_out_ingredient in sides[item.title()]["ingredients"]:
                print(f"Sorry, the {sold_out_ingredient} is sold out. Please choose a different item.")
                alternatives = similar_foods.get(item.title(), [])
                filtered_alternatives = [alt for alt in alternatives if sold_out_ingredient not in sides[alt]["ingredients"]]
                if filtered_alternatives:
                    suggestion = ", ".join(filtered_alternatives)
                    print(f"Alternative suggestion: {suggestion}")
                else:
                    not_similar_alternatives = [side.title() for side in sides if sold_out_ingredient not in sides[side]["ingredients"]]
                    suggestion = ", ".join(not_similar_alternatives)
                    print(f"No similar alternatives available. You may consider: {suggestion}")

            else:
                # after validating the item and its title, add it to the order
                existing_item = next((entry for entry in order if entry["item"] == item.title()), None)

                if existing_item:
                    # increment the quantity of the existing item
                    existing_item["quantity"] += 1
                else:
                    # add a new entry for the item with quantity 1
                    order.append({"item": item.title(), "quantity": 1})


        except EOFError:
            print("\n")
            break

    return order


def calculate_total_cost(order, menu, sides):
    # calculate total cost (P*Q per item)
    total_cost = 0

    for entry in order:
        item = entry["item"]
        quantity = entry["quantity"]

        if item in menu:
            price = menu[item]['price']
            total_cost += price * quantity
        elif item in sides:
            price = sides[item]['price']
            total_cost += price * quantity

    return total_cost


def generate_order_number():
    order_numbers = set()

    # Read previous order numbers if the file exists
    if os.path.isfile("order_number.txt"):
        with open("order_number.txt", "r") as file: #'r' = read mode
            for line in file:
                line = line.strip()
                if line and not line.isspace():  # Skip empty lines and lines with whitespace characters only
                    order_numbers.add(int(line))

    max_attempts = 100
    current_attempt = 0
    order_number = 0

    # Generate a unique order number
    while current_attempt < max_attempts:
        order_number = random.randint(1, 999)
        if order_number not in order_numbers:
            break
        current_attempt += 1
    else:
        # Raise an exception if too many attempts were made
        raise Exception("We have too many orders at the moment. Please try again later.")

    # Add the order number to the file
    with open("order_number.txt", "a") as file:
        if not order_numbers:
            file.write(f"{order_number}\n")
        else:
            file.write(f"{order_number}\n")

    return order_number


def generate_receipt(order_number, order, menu, sides, total_cost):
    # generate the filename using the order number
    filename = f"receipt-{order_number}.txt"

    receipt = ""

    # header for the order number
    receipt += f"=== Order #{order_number} ===\n"
    receipt += f"\n"

    # iterate over each item in the order
    for entry in order:
        item = entry["item"].title()
        quantity = entry["quantity"]
        if item in menu:
            price = menu[item]["price"]
        elif item in sides:
            price = sides[item]["price"]
        else:
            continue

        # calculate the total cost for the item
        item_cost = price * quantity

        # format the item, quantity, and cost
        item_line = f"{quantity} x {item} {'.' * (10 - len(item))} ${item_cost:.2f}\n"
        receipt += item_line
        receipt += f"\n"

    # add the total cost
    receipt += f"Total: ${total_cost:.2f}\n"
    receipt += f"\n"

    # formatting the receipt with equal signs
    receipt = f"====================\n{receipt}====================\n"

    # save the receipt to the specified file
    with open(filename, "w") as file:
        file.write(receipt)

    return receipt


def save_order(order_number, order, total_cost, phone_number):
    # open file; write Order Number and Phone Number
    with open("order_history.txt", "a") as file: # 'a' = append mode!
        file.write(f"Order Number: {order_number}\n")
        file.write(f"Phone Number: {phone_number}\n")
        for entry in order:
            item = entry["item"]
            quantity = entry["quantity"]
            file.write(f"{item}: {quantity}\n")
        file.write(f"Total Cost: {total_cost:.2f}\n")
        file.write("\n")


def check_order(order_number, phone_number):
    with open("order_history.txt", "r") as file:
        lines = file.readlines()
        entry_lines = []
        for line in lines:
            entry_lines.append(line)
            if line.strip() == "":
                # Reached the end of an entry
                if entry_lines[0].strip() == f"Order Number: {order_number}" and entry_lines[1].strip() == f"Phone Number: {phone_number}":
                    return entry_lines[:-1]  # Exclude the empty line
                entry_lines = []
    return None


def track_order():
    order_number = input("Enter your order number: ")
    phone_number = input("Enter your phone number: ")

    order_details = check_order(order_number, phone_number)
    if order_details:
        print("\nDuplicate Receipt:")
        for line in order_details:
            print(line.strip())
    else:
        print("Order not found.")


if __name__ == "__main__":
    main()



