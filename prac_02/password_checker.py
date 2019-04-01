"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password, SPECIAL_CHARACTERS, SPECIAL_CHARS_REQUIRED):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password, special_characters, special_chars_required):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        is_lower = char.islower()
        is_upper = char.isupper()
        is_digit = char.isdigit()
        is_special = char in special_characters
        if is_lower:
            count_lower += 1
        elif is_upper:
            count_upper += 1
        elif is_digit:
            count_digit += 1
        # Not sure whether should be an else (are there other inputs that can be taken)
        elif is_special:
            count_special += 1
    if special_chars_required:
        if count_lower >= 1 and count_upper >= 1 and count_digit >= 1 and count_special >= 1:
            return True
        else:
            return False
    else:
        if count_lower >= 1 and count_upper >= 1 and count_digit >= 1:
            return True
        else:
            return False
    # print(count_lower)
    # print(count_upper)
    # print(count_digit)
    # print(count_special)

    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()
