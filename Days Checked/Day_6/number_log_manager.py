file_path = "F:/AI/Days Checked/Day_6/numbers.txt"


def view():
    """
    Displays all stored entries from numbers.txt.
    If the file doesn't exist or is empty, print a message.
    """
    # import os
    # current_directory = os.getcwd()
    # print(
    #    f"Python is currently operating in this directory: {current_directory}")
    try:
        with open(file_path, 'r') as file_object:
            content = file_object.read()
            if not content.strip():
                print("File is empty")
            else:
                print(content)
    except FileNotFoundError:
        print("File doesn't exist")

# Use if not content: if you strictly only care about files with zero bytes of data.
# Use if not content.strip(): if you want to consider files containing only whitespace (which are usually useless in a data context) as empty files.


def add_numbers():
    """
    Prompts user for:
      - a number (must be numeric)
      - a short note (string)
    Appends "<number> - <note>" to numbers.txt.
    """
    while True:
        number = input("please input a number ")
        if number.isdigit():
            print("number added")
            break
        else:
            print("Numbers only, try again")

    short_message = input("any messages you want to add? ")
    try:
        with open(file_path, 'r') as check_file:
            existing_content = check_file.read().strip()
    except FileNotFoundError:
        existing_content = ""  # if file doesn't exist, treat as empty

    with open(file_path, 'a') as file_object:
        if existing_content:
            file_object.write("\n")
        file_object.write(f"{number} - {short_message}")


def clear_file():
    """
    Asks the user to confirm clearing all entries.
    If confirmed (Y/y), overwrites numbers.txt with nothing.
    """
    while True:
        user_confirm = input(
            "are you sure you want to clear the file? Y/y, input q or quit to go back to main menu ").lower()
        if user_confirm == 'y':
            with open(file_path, 'w') as clear:
                clear.write("")
                break
        if user_confirm in ['q', 'quit']:
            return
        else:
            print("input q or Y/y")


def menu_select():
    """
    Displays the main menu and returns the user's selection as an integer.
    Handles invalid or non-numeric input safely.
    """
    while True:
        user_input = input("which menu do you want to access? ")
        # 2. Convert the valid string digit to an integer
        menu_select = int(user_input)
        if user_input.isdigit():          # 🟩 Outer IF → only runs if input is numeric
            if menu_select in range(1, 5):  # 🟩 Inner IF → only runs for valid 1–4
                return menu_select
            else:                         # 🔸 INNER ELSE
                # handles out-of-range numbers
                print("Please select a menu between 1–4.")
        else:                             # 🔸 OUTER ELSE
            print("Numbers only, please.")  # handles non-numeric input


def main():
    """
    Main loop that:
      - prints the menu
      - asks for user choice
      - calls the correct function
      - repeats until the user quits
    """

    while True:
        print("""
 1. View Numbers
 2. Add Number
 3. Clear File
 4. Quit
              """)
        confirm = menu_select()
        if confirm == 1:
            view()
        elif confirm == 2:
            add_numbers()
        elif confirm == 3:
            clear_file()
        elif confirm == 4:
            break


# --- Program Entry Point ---
if __name__ == "__main__":
    main()
