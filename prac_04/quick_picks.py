def main():
    """Create a lotto ticket with "x" number of quickpicks"""
    number_of_quickpicks = get_number_of_quickpicks()
    # Open an empty lotto ticket list
    lotto_ticket = []
    # Place each quickpick into a spot in the list
    for quickpick in range(0, number_of_quickpicks):
        lotto_ticket.append(create_quickpick())
    # Send lotto ticket to be printed
    print_lotto_ticket(lotto_ticket, number_of_quickpicks)


def get_number_of_quickpicks():
    """Obtain number of quickpicks from user"""
    # Boolean to ensure that a valid input is made by the user
    valid_number = False
    while not valid_number:
        try:
            # Ask the user for a number of quickpicks
            number_of_quickpicks = int(input("How many quick picks? "))
            # Ensure a negative number isn't input
            if number_of_quickpicks >= 0:
                valid_number = True
            # Error message
            else:
                print("Invalid number of tickets, please input 0 or more")
        # Make sure only integers are input
        except ValueError:
            print("Not a valid integer")
    return number_of_quickpicks


def create_quickpick():
    """Create a set of 6 random numbers"""
    # Import the random module
    import random

    # Open an empty list for the 6 quick pick numbers
    quickpick_numbers = []
    for number in range(0, 6):
        # Assign a random number from 1 to 45
        quickpick_number = random.randint(1, 45)
        while quickpick_number in quickpick_numbers:
            quickpick_number = random.randint(1, 45)
        quickpick_numbers.append(quickpick_number)
    # Sort the quickpick numbers before returning
    quickpick_numbers.sort()
    return quickpick_numbers


def print_lotto_ticket(lotto_ticket, number_of_quickpicks):
    """Print lotto ticket"""
    for quickpick in range(0, number_of_quickpicks):
        for number_in_quickpick in range(0, 6):
            print("{:>2}".format(lotto_ticket[quickpick][number_in_quickpick]), end=' ')
        print("\n")


main()
