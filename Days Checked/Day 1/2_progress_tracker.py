name = input("Input player name : ")
exp = input("Input XP : ")
conv_exp = int(exp)
print(f"player : {name}")
print(f"current XP: {conv_exp}")
goal_exp = 100
added_exp = 30
total_exp = conv_exp + added_exp
print(f"gaining {added_exp} XP")
print(f"new XP Total : {total_exp} XP")
if total_exp > goal_exp:
    print(
        f"you are gaining {added_exp} you leveled up gaining {total_exp - goal_exp} bonus XP!")
else:
    print(f"you are {goal_exp - total_exp} away from leveling up!")
