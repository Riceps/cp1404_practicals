"""Jake"""
MINIMUM_LENGTH = 4  # minimum password length
valid_password = False # set a boolean password validator for while loop

# Ask user for password input
password = str(input("Enter your password: "))
while not valid_password:
    # if password does not meet length requirements, request another password
    if len(password) < MINIMUM_LENGTH:
        print("Password must contain at least 4 characters")
        password = str(input("Enter your password: "))
    else:
        valid_password = True
# Print password length as '*'
print("*" * len(password))
