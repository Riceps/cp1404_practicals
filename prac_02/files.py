"""UTILISING TEXT FILES"""
# QUESTION 1
# Create a file that stores a name
name_file = open("name.txt", 'w')
# Request a name from the user
user_name = str(input("What is your name: "))
# Prints the users name to the text file
print(user_name, file=name_file)
# Close the text file
name_file.close()

# QUESTION 2
# Read from the name text file
name_file = open("name.txt", 'r')
# Read the first line of the text file
name_from_text = name_file.readline()
# Print the name read from the text file to the terminal
print("Your name is: ", name_from_text)

# QUESTION 3
# Read from the text file containing 2 numbers
numbers_file = open("numbers.txt", 'r')
# Assign each number to a constant
first_number = int(numbers_file.readline())
second_number = int(numbers_file.readline())
# Convert the string numbers into integer numbers and add them
total_number = first_number + second_number
# Print the total number
print(total_number)
# Close the numbers file
numbers_file.close()

# QUESTION 4
# Reset total number to 0
total_number = 0
# Open file of lots of numbers to read
lots_of_numbers_file = open("lots_of_numbers.txt", 'r')
for line in lots_of_numbers_file:
    # Takes the number on each line and makes it a float
    line_number = float(line)
    # Adds each float number to the current total
    total_number += line_number
# Print final total number
print(total_number)
# Close file
lots_of_numbers_file.close()
