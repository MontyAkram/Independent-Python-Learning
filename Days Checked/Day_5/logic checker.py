def delete_task(tasks):
    """
    Removes a selected task from the list.
    Parameters:
        tasks (list): List of task dictionaries.
    """
    # Assuming view_tasks is defined elsewhere and works correctly
    # view_tasks(tasks)

    while True:
        ask_del = input(
            "Which task do you want to delete? (Type 'back' to return) ").lower()

        if ask_del == "back":
            # Exit the function if the user types 'back'
            return tasks

        task_found = False
        for task_item in tasks:
            if task_item['task'].lower() == ask_del:
                tasks.remove(task_item)
                print(f"Task '{task_item['task']}' deleted! ")
                task_found = True
                # Break the for loop after deletion
                break

        if task_found:
            # Task was found and deleted, break the while loop and exit the function
            break
        else:
            # Task not found, prompt the user again (while loop continues)
            print("Task not found! Please type the exact task name or 'back'.")

    return tasks  # Return the modified list
