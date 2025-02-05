def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Get user input
num = int(input("Enter a number to check if it's prime: "))
print(is_prime(num))  # Output: True or False
