# This function will be used to display the menu of our application.
def display_menu():
    print(" --- Objectives List Menu --- ")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove completed Tasks")
    print("5. Exit")

# This function will add a task into the Todo list.
def add_task(todo_list):
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

