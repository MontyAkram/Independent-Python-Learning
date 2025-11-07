issue_found = False
print("Scanning warehouse \n")

for aisle in range(1, 3):
    print(f"Checking aisle {aisle} \n")

    for item in ["X", "Y"]:
        if item == "X":
            print("Box X needs label")  # print that X needs label
            print("Stopping inspection \n")
            issue_found = True
            break  # maybe stop early with break
        else:
            print("Box Y is Ready")  # print that Y is ready

    else:
        print(f"aisle check {aisle} cleared \n")  # print aisle cleared
        continue  # this only runs if the inner loop wasn't broken

    break
else:
    # this only runs if the outer loop wasn't broken
    print("Warehouse check ready")  # print final warehouse ready

# after the loops, use the flag to summarize
print(f"issue is {issue_found}")
if issue_found:
    print(f"Issue found in aisle {aisle}")  # print issue found
else:
    print("all aisles processed")  # print all aisles processed
