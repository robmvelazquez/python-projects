# Initialize an empty list
my_list = []

# Take user input to populate the list
num_elements = int(input("Enter the number of elements: "))

for i in range(num_elements):
    element = input("Enter element {}: ".format(i+1))
    my_list.append(element)

# Print the original list
print("Original List:", my_list)

# Take user input to edit a specific element
index = int(input("Enter the index of the element to edit: "))
new_value = input("Enter the new value: ")

# Modify the list based on user input
if index < len(my_list):
    my_list[index] = new_value
    print("Updated List:", my_list)
else:
    print("Invalid index. Index out of range.")

