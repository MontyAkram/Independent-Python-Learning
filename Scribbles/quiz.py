score = 0
correct = 0

answer_one = str(
    input("Question 1: What is the output of print(\"Python\"[0])?"))

if answer_one.lower() == "p":
    print(f"Correct your answer is {answer_one}")
    score += 20
    correct += 1
else:
    print(f"Incorrect, your answer is {answer_one}, the correct answer is P")
    score += 0
    correct += 0

answer_two = str(
    input("Question 2: What symbol is used for exponentiation in Python?"))

if answer_two == "**":
    print(f"Correct your answer is {answer_two}")
    score += 20
    correct += 1
else:
    print(f"Incorrect, your answer is {answer_two}, the correct answer is **")
    score += 0
    correct += 0

answer_three = str(
    input("Question 3: True or False — In Python, text data must be surrounded by quotes?"))

if answer_three.lower() == "true":
    print(f"Correct your answer is {answer_three}")
    score += 20
    correct += 1
else:
    print(
        f"Incorrect, your answer is {answer_three}, the correct answer is True")
    score += 0
    correct += 0

answer_four = str(
    input("Question 4: If x = 10 and y = 3, what is x % y?"))

if answer_four == "1":
    print(f"Correct your answer is {answer_four}")
    score += 20
    correct += 1
else:
    print(f"Incorrect, your answer is {answer_four}, the correct answer is 1")
    score += 0
    correct += 0

answer_five = str(
    input("Question 5: What keyword is used to define a variable in Python?"))

if answer_five == "=":
    print(f"Correct your answer is {answer_five}")
    score += 20
    correct += 1
else:
    print(f"Incorrect, your answer is {answer_five}, the correct answer is =")
    score += 0
    correct += 0

total = correct
grade = score

print(f"You got {total} of 5 Correct!")
print("your grade is :", grade)
