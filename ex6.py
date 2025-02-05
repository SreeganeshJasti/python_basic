my_dict = {}

# Get user input for five key-value pairs
for i in range(5):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for key {key}: ")
    my_dict[key] = value

print("The dictionary is:", my_dict)
