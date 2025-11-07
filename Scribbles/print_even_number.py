total = 0
for numbers in range(1, 10):
    if numbers % 2 == 0:
        print(numbers)
        total += 1
print(f"we have {total} even numbers")
