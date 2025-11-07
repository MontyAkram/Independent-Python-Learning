base_num = input("Enter a number:")
conv_num = int(base_num)
total = 0
equation = ""

for i in range(1, conv_num + 1):
    total += i

    if i == 1:
        equation += str(i)
    else:
        equation += " + " + str(i)

print(f"{equation} = {total}")
