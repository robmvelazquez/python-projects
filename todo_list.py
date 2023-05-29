# This function will be used to display the menu of our application.
def display_menu():
    print("\n --- Objectives List Menu --- ")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove completed Tasks")
    print("5. Exit")

# This function will add a task into the Todo list.
def add_task(todo_list):
    global task
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added successfully.")

# This function will be used to view tasks.
def view_tasks(todo_list):
    print(" === Tasks === ")
    if len(todo_list) == 0:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    print()

# This function will be used to mark tasks as completed.
def mark_task_completed(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    if task_index < 0 or task_index >= len(todo_list):
        print("Invalid task number.")
    else:
        print(f"Marked task '{todo_list[task_index]}' as completed.")
        todo_list.pop(task_index)


# This function will delete completed tasks from the list.
def remove_completed_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks found.")



# This function will be used to remove completed tasks.

#This function initializes the application.
def todo_list_app():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            remove_completed_tasks(todo_list)
        else:
            print("\nInvalid choice. Please try again")

# Run the Todo list application
todo_list_app()