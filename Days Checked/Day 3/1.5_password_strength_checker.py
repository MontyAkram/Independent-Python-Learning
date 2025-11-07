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
    # set removes duplicates from the list, in this context it's the password input, i.e from P@SSSw01230RRD to P@Sw0123RD
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

    return score


while True:
    final = password_checker()
    if final != 4:
        print("\n❌ Password is invalid — see details above.")
    if final == 4:
        break

# 🧩 What You Built
#
# You created a modular, loop-driven password validation system — it checks for multiple security criteria, scores the password,
# and loops until the user meets all requirements.
#
# 🧠 Core Concepts You Practiced
# 1. Functions and Modularity
#
# Each password rule (valid_length, valid_spec_character, etc.) is its own function.
#
# This separation makes your code easy to maintain, test, and upgrade — a big step toward professional design.
#
# You used return values to pass results back to the main checker.
#
# 2. Boolean Logic
#
# You used expressions like not prompt.isalnum() and any(letter.isupper() for letter in letters) to evaluate conditions.
#
# Each validator returns True or False, making it composable and simple to sum for scoring.
#
# 3. Loop Control (while True + break)
#
# The loop keeps running until the password passes all tests (score == 4).
#
# break cleanly exits once success criteria are met — no recursion, no repeated calls.
#
# This is a classic input validation pattern used in login systems, data entry forms, etc.
#
# 4. Validation Feedback
#
# Each failed check prints a clear, human-readable message.
#
# You also added graded feedback — Weak / Medium / Strong — teaching you how to use logic branching for UX.
#
# 5. Return Values for State Tracking
#
# password_checker() returns a numeric score, allowing the outer loop to make decisions.
#
# This taught you how functions can return data for higher-level logic — a key step toward modular design.
#
# 🧮 Flow Summary
#
# User enters password.
#
# Each rule runs once and returns True/False.
#
# Total score (0–4) is computed.
#
# Program reports strength and errors.
#
# If score < 4 → loop repeats, prompting again.
#
# If score = 4 → success message, loop exits.
#
# 🏆 Skills Gained
#
# ✅ Function composition
# ✅ Boolean conditions and loops
# ✅ Logical control flow with break
# ✅ Input validation pattern used in real systems
# ✅ Clean, maintainable structure without recursion
#
# 💡 Next Upgrade (Password Checker 3.0 idea)
#
# If you want to level this up next:
#
# Add color-coded output using colorama or termcolor.
#
# Store passwords securely (hash simulation).
#
# Track how many attempts the user made before success.
