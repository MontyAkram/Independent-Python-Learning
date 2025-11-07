Number = 7
while True:
    command = int(input("I'm thinking of a number, what's your guess? "))
    print("Gotcha it's Number lucky", command)
    if command < Number:
        print("Too low low low low apple bottom jeans, boots with the furrrrrr")
    elif command > Number:
        print("Too high, what are you? the moon?")
    else:
        break

print("you got it, you'll get a job after you finish this course, hopefully")
