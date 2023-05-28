my_list = []

# Prompts for user input
user_input = input("Enter a task description: ")
while user_input != 'done':
    my_list.append(user_input)
    user_input = input("Enter another item (or 'done' when finished): ")

# Prints the final list
print("Final list: ", my_list)