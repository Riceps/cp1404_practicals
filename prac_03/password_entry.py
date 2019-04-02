def main():
    """Password Checker"""
    # Ask user for password input
    password = get_password()
    # Print password length as '*'
    print_password(password)


def get_password():
    """Retrieve password from user"""
    valid_password = False  # set a boolean password validator for while loop
    MINIMUM_LENGTH = 4  # minimum password length

    password = str(input("Enter your password: "))
    while not valid_password:
        # if password does not meet length requirements, request another password
        if len(password) < MINIMUM_LENGTH:
            print("Password must contain at least 4 characters")
            password = str(input("Enter your password: "))
        # If password meets length requirements exit while loop
        else:
            valid_password = True
    # Return the approved password to main
    return password


def print_password(password):
    """Print password as asterisk"""
    # Multiply asterisk by the length of password
    print("*" * len(password))
    return


main()
