def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Get user input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))
