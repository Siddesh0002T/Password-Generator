import random
import string

# Define a function to generate a password
def createPass(length):

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Return the generated password
    return password

# Ask the user for the password length
length = int(input("Enter the length of the password: "))

# Generate and print the password
print("Generated Password:", createPass(length))