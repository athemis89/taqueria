# taqueria

This project simulates a restaurant's ordering system. It provides a user-friendly, command-line interface where customers can select items from a menu. The program handles ingredient availability, generates an order number, calculates the total price, and stores the order for future reference. 

## HOW IT WORKS IN PRACTICE:

![image](https://github.com/athemis89/taqueria/assets/121729165/b05b13b9-d332-42cb-a3d3-84920a15112f)



## HOW THE CODE WORKS

**initalising the menu and sides**

![Screenshot 2023-06-16 at 14 53 59](https://github.com/athemis89/taqueria/assets/121729165/9bf441fb-0d97-431a-9fa8-e5327e4440ff)

The code defines two dictionaries: menu and sides. 
These dictionaries represent the available food items on the menu and their respective prices and ingredients.

**main() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/435f5136-c23b-44f2-b862-be7138863294)

The main() function serves as the entry point of the program. 
It prompts the user to select an option: "New Order" or "Track Order." 
Based on the user's input, it calls the corresponding functions: new_order() or track_order().

**welcome() funtion**

![image](https://github.com/athemis89/taqueria/assets/121729165/4ebbcd8d-1e80-4d2c-ba5c-ae3d218597e9)

The welcome() function displays a welcome message and asks the user to enter their postcode for delivery. 
It then shows the available menu items and sides along with their prices.
Lastly, it instructs the user to write down their order and enter "done" when they have finished.

**new_order() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/ab5f8552-21e4-402e-839a-094ab8fcd211)

The new_order() function handles the process of placing a new order.
It calls the welcome() function to display the menu and prompt the user for their order.
It receives the order details from the place_order() function.
It generates an order number, calculates the total cost, and determines the estimated delivery time.
It asks the user to confirm the order by providing their phone number.
It calls the generate_receipt() and save_order() functions, and finally opens the resulting receipt file for the client.

**place_order() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/5d1a93c9-15a3-49ce-9cba-e40335d01a03)
![image](https://github.com/athemis89/taqueria/assets/121729165/2f5fae4f-f5dc-4846-ab69-132a797d168b)

The place_order() function is responsible for taking the user's order.
It randomly selects an ingredient to be "sold out."
It prompts the user to enter items from the menu or sides until they enter "done" to finish.
If the selected item is sold out, it offers alternative suggestions.
It keeps track of the order and quantity, and returns the order details.

**calculate_total_cost() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/d0fc3517-8b12-4456-a22b-c9f2c1fa6440)

The calculate_total_cost() function calculates the total cost of the order based on the item prices and quantities.
It iterates over each item in the order and retrieves its price from the menu or sides dictionary.
It multiplies the price by the quantity and adds up the total cost.

**generate_order_number() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/dbb32692-cdb0-49af-b000-a4648fef5ada)

The generate_order_number() function generates a unique order number.
It reads previous order numbers from a file.
It attempts to generate a random order number and checks if it's unique.
If too many attempts are made, it raises an exception.
It adds the order number to the file and returns the generated order number.

**generate_receipt() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/20a9fbce-1f1e-4506-88f6-7db0d13f3bb2)

The generate_receipt() function generates a receipt for the order.
It takes the order number, order details, menu, sides, and total cost as input.
It formats the receipt with the order number, each item in the order with its quantity and cost, and the total cost.
It saves the receipt to a file and returns the generated receipt.

**save_order() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/899a43f2-229a-44bf-9527-206c4d8aaa45)

The save_order() function saves the order details to a file.
It takes the order number, order details, total cost, and phone number as input.
It opens the file in append mode and writes the order number, phone number, each item in the order with its quantity, and the total cost.

**check_order() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/588aa5b7-815e-406c-9eb3-f42d9baa4846)

The check_order() function is used to check an order in the order history based on the order number and phone number.
It opens the "order_history.txt" file in read mode. It reads all the lines from the file using the readlines() method and stores them in the lines list.
It initializes an empty list called entry_lines to store the lines of each entry. It iterates through each line in the lines list. It appends each line to the entry_lines list.
When it encounters a line that is empty (denoting the end of an entry), it checks if the first line of the entry matches the given order_number and the second line matches the given phone_number.
If there is a match, it returns the entry_lines list without the empty line. If no match is found, it clears the entry_lines list and continues searching for another entry.
If the end of the file is reached and no match is found, it returns None to indicate that the order was not found.

**track_order() function**

![image](https://github.com/athemis89/taqueria/assets/121729165/a417716c-ca38-4f44-9515-6acbd0c01cb5)

The track_order() function allows the user to track their order by entering their order number and phone number.
It prompts the user to enter their order number and phone number.
Calling the check_order () function, it reads the order details from the file and checks if the entered order number and phone number match.
If a match is found, it displays the order details.
If no match is found, it informs the user that the order was not found.




