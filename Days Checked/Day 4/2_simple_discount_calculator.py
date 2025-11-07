# If total is over 100 → 10% discount
# If total is over 50 but ≤ 100 → 5% discount
# Otherwise → no discount

def get_purchase_amount():
    """
    Asks the user for their total purchase amount.
    Returns:
        float: The total purchase amount entered by the user.
    """
    # Step 1: Ask user for total purchase amount
    try:
        price_amount = float(input("How much did you buy it for? "))
        return price_amount
    except ValueError:
        print("Invalid number, please try again.")
        return get_purchase_amount()  # ask again recursively


def calculate_discount(amount):
    """
    Determines the discount based on the purchase amount.
    Parameters:
        amount (float): The total purchase amount.
    Returns:
        float: The discount amount to apply.
    """
    # Step 2: Apply conditions for discount tiers
    if amount >= 100:
        discount = amount * 0.10
    elif 50 <= amount <= 99:
        discount = amount * 0.05
    else:
        discount = 0
    return discount


def show_final_amount(amount, discount):
    """
    Displays the total amount after discount.
    Parameters:
        amount (float): Original purchase amount.
        discount (float): Discount amount.
    """
    # Step 3: Calculate and display the final total
    final = amount - discount
    return final


def discount_calculator():
    """
    Main function to run the discount calculator.
    """
    # Step 1: Get purchase amount
    amount_1 = get_purchase_amount()
    # Step 2: Calculate discount
    discount_1 = calculate_discount(amount_1)
    final_1 = show_final_amount(amount_1, discount_1)
    # Step 3: Display final total
    print(f"Your total after discount is: ${final_1:.2f}")


discount_calculator()
