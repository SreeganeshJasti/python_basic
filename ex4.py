def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Get user input
print("Enter two numbers:")
x = float(input("First number: "))
y = float(input("Second number: "))

print("Select operation: 1. Add 2. Subtract 3. Multiply 4. Divide")
choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", add(x, y))
elif choice == '2':
    print("Result:", subtract(x, y))
elif choice == '3':
    print("Result:", multiply(x, y))
elif choice == '4':
    print("Result:", divide(x, y))
else:
    print("Invalid input")
