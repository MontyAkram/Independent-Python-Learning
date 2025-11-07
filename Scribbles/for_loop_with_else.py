# for number in range(1, 6):
#    print(f"row {number}:", number * "*")
# successful = False
# for number in range(1, 4):
#    print(f"Attempt {number}")
#    if number == 4:
#        successful = True
#    if successful:
#        print("huh")
#        break
# else:
#    print("All attempts finished - process complete")

# successful = False
# for number in range(1, 7):
#    print(f"Attempt {number}")
#    if number == 5:      # you "succeed" on attempt 2
#        successful = True
#    if successful:
#        print("huh")
#        break
# else:
#    print("All attempts finished - process complete")

found_even = True

for n in range(1, 6):          # loop layer
    if n % 2 == 0:              # decision layer
        print(f"{n} is even")
        found_even = True
        break                   # stops the loop early
    else:
        print(f"{n} is odd")    # runs for every odd
else:
    # runs only if loop finishes with NO break
    print("No even numbers were found")
