def menu_select():
    user_input = input("Which menu are you trying to access? (1–5) ")
    if not user_input.isdigit():
        print("⚠️ Please enter a valid number between 1–5.")
        return 0
    menu = int(user_input)
    if menu not in range(1, 6):
        print("⚠️ Please enter a number between 1 and 5.")
        return 0
    return menu


def add_item(cart):
    """
    Adds an item to the shopping cart.
    Parameters:
        cart (list): Current shopping cart list
    Returns:
        list: Updated shopping cart
    """

    # Step 1: Ask user for item name
    item_name = input("what's the item? ")

    # Step 2: Ask user for item price safely
    try:
        item_price = float(input("Please input the price: "))
    except ValueError:
        print("⚠️ Invalid input! Price must be a number.")
        return cart  # cancel and return the unchanged cart

    # Step 3: Ask user for quantity safely
    try:
        item_quant = int(input("How many are you buying? "))
    except ValueError:
        print("⚠️ Invalid input! Quantity must be a whole number.")
        return cart
    # Step 4: Create a dictionary for the item
    item = {
        "name": item_name,
        "price": item_price,
        "quantity": item_quant,
    }
    # Step 5: Append the dictionary to the cart
    cart.append(item)
    print(f"✅ {item_name} added ({item_quant} pcs @ ${item_price:.2f})\n")
    # Step 6: Return the updated cart
    return cart


def view_cart(cart):
    """
    Displays all items currently in the shopping cart.
    Parameters:
        cart (list): The current shopping cart list
    Returns:
        None
    """
    # Step 1: Check if the cart is empty
    print("This is your current cart")
    if not cart:
        print("Doesn't have any items")
        return
    # Step 2: If not empty, print each item in a readable format
    else:
        for item in cart:
            print(
                f"{item['name']} - ${item['price']:.2f} x {item['quantity']} = ${item['price'] * item['quantity']:.2f}")


def calculate_total(cart):
    """
    Calculates and returns the total cost of all items in the cart.
    Parameters:
        cart (list): The current shopping cart list
    Returns:
        float: The total cost of all items
    """
    # Step 1: Initialize a total variable
    total_sum = 0
    # Step 2: Loop through the cart to accumulate the total
    for items in (cart):
        total_sum += items["price"] * items["quantity"]
    # Step 3: Return the total
    return total_sum


def remove_item(cart):
    """
    Removes an item from the shopping cart by name.
    Parameters:
        cart (list): The current shopping cart list
    Returns:
        list: The updated cart after removal
    """
    print("This is your current cart:")
    view_cart(cart)

    inquire = input("Which item do you want to remove? ")

    for item in cart:
        if item["name"] == inquire:
            cart.remove(item)
            print(f"{inquire} has been removed.")
            break  # optional: stop after removing the first match

    print("This is your updated cart:")
    view_cart(cart)

    return cart


def main():
    """
    Main function to run the shopping cart program.
    Provides a menu for user interaction.
    """
    # Step 1: Initialize an empty cart
    cart = []
    # Step 2: Create a loop to keep showing the menu until the user exits
    while True:
        # Step 3: Show menu options (1–5)
        print(""" 1.Add items 
 2.View your cart 
 3.Calculate your shopping list
 4.Remove your item
 5.quit""")
    # Step 4: Ask the user for their choice
        main_menu = menu_select()
    # Step 5: Match the choice with the correct function call
        if main_menu == 1:
            add_item(cart)
        elif main_menu == 2:
            view_cart(cart)
        elif main_menu == 3:
            view_cart(cart)
            total = calculate_total(cart)
            print(f"Your current total is ${total} \n")
        elif main_menu == 4:
            remove_item(cart)
    # Step 6: Break the loop if user chooses to exit
        elif main_menu == 5:
            break


main()

# 🧾 Summary — What You’ve Learned So Far
# 🎯 Project: Simple Shopping Cart Calculator
#
# Core Concepts You Mastered:
#
# Modular Design(Functions):
#
# You broke a large problem(“manage a cart”) into small, clear, reusable functions.
#
# This is the foundation of software architecture — key in any AI pipeline.
#
# Lists and Dictionaries:
#
# You stored structured data(cart list containing item dicts).
#
# This concept maps directly to JSON and data serialization, both used in AI input/output formats.
#
# Loops and Conditionals:
#
# Created interactive menus with while True, controlling logic with if / elif / else .
#
# You now understand control flow, a cornerstone in LLM tool logic orchestration.
#
# Error Handling with try / except:
#
# Prevents crashes, improves robustness — essential when dealing with unpredictable user or model inputs.
#
# User Interaction:
#
# Input/output design using print() and input().
#
# This mirrors the conversational flow of LLM command-line prototypes.
#
# Composability:
#
# You learned how functions communicate via return values(cart being passed around).
#
# That’s precisely how data pipelines in AI systems chain results between modules.
#
# 🧩 Where You Can Apply This in LLM / AGI Context
# Concept	Real-world LLM/AGI Parallel
# Cart(list of dicts)	A memory buffer or conversation history storage
# Functions	Modular “tools” the LLM can call(like add_item → add_note)
# Error Handling	Preventing malformed data or invalid model output
# Menu Navigation	Command routing in chat agents or tool selection logic
# Calculate Total	Aggregation logic in reasoning chains or data post-processing
#
# You’ve essentially built your first interactive agent loop — this structure is the same idea behind a command-line chatbot or AI assistant core.
