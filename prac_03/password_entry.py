MINIMUM_LENGTH = 4  # minimum password length


def main():
    """Password Checker"""
    # Ask user for password input
    password = get_password()
    # Print password length as '*'
    print_password(password)


def get_password():
    """Retrieve password from user"""
    valid_password = False  # set a boolean password validator for while loop

    password = input("Enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        # if password does not meet length requirements, request another password
            print("Password must contain at least 4 characters")
            password = input("Enter your password: ")
    # Return the approved password to main
    return password


def print_password(password):
    """Print password as asterisk"""
    # Multiply asterisk by the length of password
    print("*" * len(password))


main()
