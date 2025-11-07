def menu_select():
    user_input = input("Which menu are you trying to access? (1–5) ")
    if not user_input.isdigit():
        print("⚠️  Please enter a valid number between 1–5.")
        return 0
    menu = int(user_input)
    if menu not in range(1, 6):
        print("⚠️  Please enter a number between 1 and 5.")
        return 0
    return menu


def add_item(local_add_cart):
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
        return local_add_cart  # cancel and return the unchanged cart

    # Step 3: Ask user for quantity safely
    try:
        item_quant = int(input("How many are you buying? "))
    except ValueError:
        print("⚠️ Invalid input! Quantity must be a whole number.")
        return local_add_cart
    # Step 4: Create a dictionary for the item
    item = {
        "name": item_name,
        "price": item_price,
        "quantity": item_quant,
    }
    # Step 5: Append the dictionary to the cart
    local_add_cart.append(item)
    print(f"✅ {item_name} added ({item_quant} pcs @ ${item_price:.2f})\n")
    # Step 6: Return the updated cart

    return local_add_cart


def view_cart(local_view_cart):
    """
    Displays all items currently in the shopping cart.
    Parameters:
        cart (list): The current shopping cart list
    Returns:
        None
    """
    # Step 1: Check if the cart is empty
    if not local_view_cart:
        print("Cart doesn't have any items")
        return
    # Step 2: If not empty, print each item in a readable format
    else:
        print("This is your current cart")
        for local_item in local_view_cart:
            print(
                f"{local_item['name']} - ${local_item['price']:.2f} x {local_item['quantity']} = ${local_item['price'] * local_item['quantity']:.2f}\n")


def calculate_total(local_total_cart):
    """
    Calculates and returns the total cost of all items in the cart.
    Parameters:
        cart (list): The current shopping cart list
    Returns:
        float: The total cost of all items
    """
    # Step 1: Initialize a total variable
    local_total_sum = 0
    # Step 2: Loop through the cart to accumulate the total
    for local_total_items in (local_total_cart):
        local_total_sum += local_total_items["price"] * \
            local_total_items["quantity"]
    # Step 3: Return the total
    return local_total_sum


def remove_item(local_remove_cart):
    view_cart(local_remove_cart)
    if not local_remove_cart:
        return local_remove_cart

    inquire = input("Which item do you want to remove? ").lower()
    removed = False

    for item in local_remove_cart:
        if item["name"].lower() == inquire:
            local_remove_cart.remove(item)
            print(f"\n✅ {item['name']} has been removed.\n")
            removed = True
            break

    if not removed:
        print("\n⚠️ Item not found, cart unchanged.\n")

    view_cart(local_remove_cart)
    return local_remove_cart


def main():
    """
    Main function to run the shopping cart program.
    Provides a menu for user interaction.
    """
    # Step 1: Initialize an empty cart
    main_cart = []
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
            add_item(main_cart)
        elif main_menu == 2:
            view_cart(main_cart)
        elif main_menu == 3:
            view_cart(main_cart)
            total = calculate_total(main_cart)
            print(f"Your current total is ${total} \n")
        elif main_menu == 4:
            remove_item(main_cart)
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
