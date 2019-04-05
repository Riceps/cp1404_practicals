"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        favourite_number = int(input("what is your favourite number: "))
        finished = True
        # TODO: this line
        # TODO: this line
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Your favourite number is: ", favourite_number)
