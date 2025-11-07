issue_found = False

print("Starting Server Checks")

for group in range(1, 3):
    print(f"Checking group {group}")

    for servers in ["B"]:

        if servers == "A":
            print(f"checking server {servers}")
            print(f"problem found in server {servers} — stopping inspection")
            issue_found = True
            break
        else:
            print(f"checking server {servers}\n")

    else:
        print(f"group check {group} cleared \n")  # print aisle cleared
        continue  # this only runs if the inner loop wasn't broken
    break

else:
    print(f"All groups processed – system stable")


if issue_found:
    print("Issue found – inspection stopped")
