import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Generate the password
generated_password = generate_password(password_length)

# Display the generated password
print("Generated Password:", generated_password)
