def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get user input
n = int(input("Enter how many Fibonacci numbers you want to generate: "))
for i in range(n):
    print(fibonacci(i))
