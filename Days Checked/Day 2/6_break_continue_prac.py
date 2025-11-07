print("Checking Items")
for items in range(1, 4):
    if items == 2:
        print(f"Skipping item {items}")
        continue
    if items == 3:
        print(f"item {items} broken - stopping check")
        print("Inspection Stopped early")
        break
    else:
        print(f"Item {items} ok")
