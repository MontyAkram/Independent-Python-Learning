def menu_select():
    # ask for user input
    user_input = input("Which menu do you want to access? ")
    # if not numbers, return 0 (we dont have a menu that is accessible by 0)
    if not user_input.isdigit():
        print(" numbers only!, 1-5 !\n")
        return 0
    # converts user input to integer and if the menu isn't between 1-6, return 0
    digit_select = int(user_input)
    if digit_select not in range(1, 6):
        print(" 1-5 only!\n")
        return 0
    return digit_select


def add_task(tasks):
    # asks for user input again
    task_name = input("What's the task you have in mind? ")
    # loops and asks for Y / N, other inputs will always loop
    while True:
        status = input("Has it been done yet? N/Y ").upper()
        if status in ("Y", "N"):
            break
        print("Y / N only")
    # if conditions met, insert user input to task_list dictionary
    task_list = {
        "task": task_name,
        "status": status
    }
    # parameter.append(task_list), adds the user input into the parameter which is a dictionary
    tasks.append(task_list)
    return tasks


def view_tasks(tasks):
    """
    Displays all tasks in the list.
    Parameters:
        task_list (list): List of task dictionaries.
    """
    # if empty → print message
    if not tasks:
        print("there's nothing there!")
        return  # stops here, avoids unnecessary looping
    # otherwise → loop and print tasks nicely
    for index, viewed in enumerate(tasks, 1):
        print(f"{index}. {viewed['task']} [{viewed['status']}]")
    # for index, viewed in enumerate(tasks, 1):
    #    print(f"{index}. {viewed['task']}, [{viewed['status']}]")


def mark_task_done(tasks):
    """
    Marks a selected task as done.
    Parameters:
        task_list (list): List of task dictionaries.
    """
    # show tasks before update
    print("These are your tasks so far: ")
    view_tasks(tasks)
    # ask which task number/name to mark
    mark_task_inquiry = input("Which task do you want to be marked as done? ")
    # set a flag to be used later
    is_found = False
    # with for loop, update status to "Y"
    for task_name in tasks:
        # search up the task
        # if task found and already Y, do nothing
        if mark_task_inquiry.isdigit():
            index = int(mark_task_inquiry) - 1
            if 0 <= index < len(tasks):
                task_name = tasks[index]["task"]
                tasks[index]["status"] = "Y"
                print(f"Task '{task_name}' marked as done!")
                is_found = True
                break
            # if task found and status = N, updates to Y
            else:
                print("task not found")
                # set flag to True then break
                break

    # flag is False, print the message
    if not is_found:
        print("Can't find the task")

    # show tasks after update
    print("Current task list")
    view_tasks(tasks)
    return (tasks)


def delete_task(tasks):
    """
    Removes a selected task from the list.
    Parameters:
        task_list (list): List of task dictionaries.
    """
    # while True:
    #    status = input("Has it been done yet? N/Y ").upper()
    #    if status in ("Y", "N"):
    #        break
    #    print("Y / N only")

    # show tasks
    view_tasks(tasks)
    # ask which one to delete
    while True:
        ask_del = input("Which task do you want to delete? ").lower()
    # remove from list
        if ask_del == "back":
            return
        if not ask_del.isdigit():
            print("Please enter a valid number or 'back'.")
            continue
        task_is_found = False
        index = int(ask_del) - 1
        print(f"index is {index}")
        if 0 <= index < len(tasks):
            deleted_task_item = tasks.pop(index)
            # Now we can immediately confirm what was deleted
            print(f"Task '{deleted_task_item['task']}' deleted! ")
            task_is_found = True
        if task_is_found:
            # Task was found and deleted, break the while loop and exit the function
            break
        else:
            # Task not found, prompt the user again (while loop continues)
            print("Task not found! Please type the exact task name or 'back'.")
    print("Updated task list")
    view_tasks(tasks)
    return tasks


# Without your if task_is_found block, your while True: loop never breaks —
# and because of that, the code after the loop (like return tasks or view_tasks(tasks)) can never be reached.
#
# Python’s logic is:
#
# while True:
#    # keeps looping forever unless 'break' or 'return' happens inside
# anything here is unreachable if there's no way to exit that loop
#
#
# So:
#
# When you include
#
# if task_is_found:
#    breaka
#
#
# the loop now has a valid exit path → Python knows that eventually it can get past the loop and reach return tasks. ✅
#
# When you remove that, the loop runs forever with no guaranteed exit, so Python marks the return tasks below it as unreachable code — even if it might technically never execute due to user behavior.

def main():
    """
    Main program loop.
    """
    # create empty list: tasks = []
    tasks = []
    # while True:
    while True:
        # print menu (1–5)
        print(""" 1.Add tasks
 2.View tasks 
 3.Mark tasks as done
 4.Remove task
 5.quit""")
    # get user input
        try:
            user_input = menu_select()
        except ValueError:
            print("Numbers only!")
    # match input → call functions
        if user_input == 1:
            add_task(tasks)
        elif user_input == 2:
            view_tasks(tasks)
        elif user_input == 3:
            mark_task_done(tasks)
        elif user_input == 4:
            delete_task(tasks)
        elif user_input == 5:
            break
    # break if quitting


# run the program
if __name__ == "__main__":
    main()

# ✅ Summary: What You Learned From This Project
# 1. Functions Make Code Reusable
#
# You designed the program as small pieces of logic:
#
# add_task() adds tasks
#
# view_tasks() displays them
#
# mark_task_done() updates them
#
# delete_task() removes them
#
# main() controls the flow
#
# This is modular design, the basis of scalable software and AI tool dispatch systems.
#
# 2. Passing and Updating Shared Data
#
# Your task list (main_task_list) is passed to functions and updated by them.
#
# You learned how:
#
# local_list.append(item)
#
#
# modifies data in place, so changes persist across functions.
#
# This mirrors how memory buffers and context states work in AI agents.
#
# 3. Input Validation & Control Flow
#
# You used:
#
# while True loops
#
# break
#
# input checks (if status in ("Y","N"))
#
# early returns (if ask_del == "back": return)
#
# This means you now control program flow consciously — not just writing code until it works.
#
# 4. Conditionals (if/elif/else) Structuring Logic
#
# You wrote logic that:
#
# checks valid menu choices
#
# prevents invalid states
#
# updates only when correct matches occur
#
# This is the core of decision-making, the same kind used in rule-based agents.
#
# 5. Lists & Dictionaries as Structured Data
#
# You stored tasks like this:
#
# {"task": "Laundry", "status": "N"}
#
#
# You now understand:
#
# lists = collections of structured items
#
# dicts = named data fields
#
# This is exactly how JSON works, and JSON is the native language of LLM tool interaction.
#
# 🎉 You Earned Real Bragging Rights
#
# This wasn’t copy/paste coding — it was:
#
# reasoning
#
# fixing
#
# restructuring
#
# debugging
#
# and owning the logic
#
# This is actual programming skill growth.
#
# You’re not memorizing syntax anymore.
# You’re thinking like code.
