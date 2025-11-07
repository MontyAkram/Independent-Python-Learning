def get_password():
    return input("Enter your password: ")


def valid_length(prompt):
    sufficient_length = len(prompt) >= 8

    if not sufficient_length:
        print("password must be at least 8 characters!")

    return sufficient_length


def count_digits(prompt):
    return sum(1 for character in prompt if character.isdigit())


def valid_spec_character(prompt):
    correct_char = not prompt.isalnum()

    if not correct_char:
        print("your password doesn't contain special characters")

    return correct_char


def valid_password_mix_case(prompt):
    letters = set(prompt)

    lower = any(letter.islower() for letter in letters)
    upper = any(letter.isupper() for letter in letters)

    if not upper:
        print("your password doesn't contain upper characters")
    if not lower:
        print("your password doesn't contain lower characters")

    return upper and lower


def valid_pass_num_digits(prompt):
    sufficient_digits = count_digits(prompt) >= 1
    if not sufficient_digits:
        print("doesn't have sufficient digits")

    return sufficient_digits


def password_checker():
    prompt = get_password()

    # Run each validator once and store results
    has_digits = valid_pass_num_digits(prompt)
    has_special = valid_spec_character(prompt)
    has_mix_case = valid_password_mix_case(prompt)
    has_length = valid_length(prompt)

    # Feedback messages
    if not has_length:
        print("❌ Password must be at least 8 characters.")
    if not has_digits:
        print("❌ Password must contain at least one number.")
    if not has_special:
        print("❌ Password must include a special character (!, @, #, etc).")
    if not has_mix_case:
        print("❌ Password must have both uppercase and lowercase letters.")

    # Scoring
    score = sum([has_digits, has_special, has_mix_case, has_length])

    print(f"Password strength score: {score}")
    if score == 4:
        print("Strength: Strong 💪")
    elif 2 <= score <= 3:
        print("Strength: Medium 🔐")
    else:
        print("Strength: Weak ⚠️")

    while score != 4:
        print("\n❌ Password is invalid — see details above.")
        score = password_checker()
        if score == 4:
            break

    # Output summary
    # if score == 4:
    #    print("\n✅ Password is valid and strong!")
    # else:
    #    print("\n❌ Password is invalid — see details above.")

    return score


password_checker()

# This turned out great — you actually covered a lot of core Python fundamentals and design concepts with this one project.
# Here’s a breakdown of what you learned and practiced through your password strength checker 👇
#
# 🧱 1. Functions and Modularity
#
# You split your program into small, reusable functions like valid_length(), valid_spec_character(), etc.
#
# Each one does one clear job (known as the single-responsibility principle).
#
# This makes debugging and extending the code much easier — for example, you can easily add a new rule like valid_no_spaces().
#
# 🔁 2. Return Values and Function Communication
#
# You learned that using return lets one function send data (like score) back to where it was called.
#
# For example:
#
# score = password_checker() << this one is called inside the while function
#
# assigns whatever password_checker() returned into the variable score.
#
# This was key to fixing your while loop — otherwise the score inside the loop would never update.
#
# 📦 3. Booleans and Conditional Logic
#
# Each validator returns a boolean (True or False).
#
# Then you combine them in the main function to calculate a total score using:
#
# score = sum([has_digits, has_special, has_mix_case, has_length])
#
#
# Since True = 1 and False = 0 in Python, this neatly counts how many checks passed.
#
# 🔍 4. String Methods
#
# You used several powerful built-in string methods:
#
# .isdigit() → checks if a character is a number
#
# .isalpha() and .isalnum() → check if text is letters/numbers only
#
# .islower() / .isupper() → check letter case
#
# len() → measures password length
# You now understand how these can be mixed to test real-world inputs.
#
# ⚙️ 5. Sets and Iterables
#
# You used letters = set(prompt) — this removes duplicates and speeds up case checking.
#
# Using any() with a generator expression like:
#
# any(letter.islower() for letter in letters)
#
#
# taught you lazy evaluation — Python stops checking once it finds one match, which makes it efficient.
#
# 🔄 6. Loops and Recursion
#
# Your while score != 4: loop keeps asking for a password until it’s strong enough.
#
# Inside it, you call password_checker() again, making it recurse (the function calls itself).
#
# You learned that recursion only works correctly when you return values, so the new result replaces the old one (score = password_checker()).
#
# 💬 7. User Feedback & Debugging
#
# You built feedback that explains why the password failed — a real-world UX touch.
#
# You also learned that printing inside functions can cause duplicate outputs, and that it’s better to separate logic (return) and display
#
# (print) when possible.
#
# 🧠 8. Good Design Practices
#
# You unknowingly followed several software design principles:
#
# Modularity: breaking into small testable parts
#
# Reusability: each check can be reused in other scripts
#
# Clarity: readable function names
#
# Separation of concerns: validation logic separated from user interaction
#
# 🏁 Summary Takeaways
# Concept	What You Learned
# Functions	Structure programs into reusable chunks
# Return values	How data flows between functions
# Booleans	Combine True/False values for scoring
# String methods	Inspect and validate user text
# Sets & any()	Efficient membership and property checks
# Loops	Keep retrying until condition met
# Recursion	Function calling itself for reattempts
# Clean design	Write readable, maintainable Python
#
# If you want, I can show you how to refactor this script next into a non-recursive version (using only loops), which is cleaner and avoids double calls — a great next step toward professional Python design.
# Would you like that?
