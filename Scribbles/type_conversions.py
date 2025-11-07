user_input = input("Enter a number: ")
print(f"you typed {user_input} which is stored as {type(user_input)}")
converted = int(user_input)
print(f"converted to int: {converted}")
added = converted + 3
print(f"adding 3 gives: {added}")
reverted = str(added)
print(f"Converted back to string: {reverted}")

user_input = input("Enter a number: ")
print(f'You typed "{user_input}" which is stored as {type(user_input)}')
converted = int(user_input)
print(f"Converted to int: {converted}")
added = converted + 3
print(f"Adding 3 gives: {added}")
reverted = str(added)
print(f'Converted back to string: "{reverted}"')