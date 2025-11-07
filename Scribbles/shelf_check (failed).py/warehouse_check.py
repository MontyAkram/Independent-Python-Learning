print("Scanning warehouse")
for aisle in range(1, 3):
    print(f"Checking aisle {aisle}")

    for item in ["X", "Y"]:
        if item == "X":
            print("Box X requires label - stopping inspection")
            break   # 🚨 stop inner loop immediately if X needs a label
        else:
            print("Box Y ready for shipping")
    else:
        # only runs if inner loop wasn't broken
        print(f"Aisle {aisle} cleared \n")
        continue  # move on to next aisle

    # if we broke out of inner loop, break outer too
    break
else:
    # only runs if outer loop wasn't broken
    print("All aisles processed - warehouse ready")
