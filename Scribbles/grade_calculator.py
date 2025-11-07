student_name = str(input("Enter Name : "))
score = int(input("Enter Score : "))

print("====================")
print("STUDENT REPORT")
print("====================")


print("Name : ", student_name.upper())
print("Score: ", score)
if score < 0 or score > 100:
    print("Wrong score!")
elif score == 100:
    print("Grade : A, Perfect Score!")
elif 90 <= score <= 99:
    print("Grade : A")
elif 80 <= score <= 89:
    print("Grade : B")
elif 70 <= score <= 79:
    print("Grade : C")
elif 60 <= score <= 69:
    print("Grade : D")
else:
    print("Grade : F")
print("====================")
