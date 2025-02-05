import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

# Get user input for password length
length = int(input("Enter the length of the password: "))
print("Generated password:", generate_password(length))
