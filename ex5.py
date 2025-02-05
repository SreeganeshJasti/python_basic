def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Get user input
lst = input("Enter numbers separated by space: ").split()
lst = [int(x) for x in lst]  # Convert to integers
print("List without duplicates:", remove_duplicates(lst))
