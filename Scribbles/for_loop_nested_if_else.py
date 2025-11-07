# found_even = False
# for n in range(1, 6, 2):
#    if n % 2 == 0:
#        print(f"Number {n} is Even - break triggered")
#        found_even = True
#        break
#    else:
#        print(f"Number {n} is odd")
# else:
#    print("All Numbers checked - no even numbers found")

found_even = False

for n in range(1, 6):  # add another condition to trigger odd only (add ,2 after 6)
    if n % 2 == 0:
        print(f"Number {n} is even - break triggered")
        found_even = True
        break
    else:
        print(f"Number {n} is odd")
else:
    print("All Numbers checked - no even numbers found")

# now we consult the flag
if found_even:
    print("Inspection stopped early")
else:
    print("Finished inspection without finding evens")
