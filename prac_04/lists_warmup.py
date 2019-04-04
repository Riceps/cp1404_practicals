numbers = [3, 1, 4, 1, 5, 9, 2]

# Obtains the item in the 0th spot (3)
print(numbers[0])
# Obtains the item in the last spot (2)
print(numbers[-1])
# Obtains the item in the 3th spot (1)
print(numbers[3])
# Obtains all the numbers from the 0th spot to the last spot (last spot non-inclusive) [3,1,4,1,5,9]
print(numbers[:-1])
# Obtains all the numbers from the 3th spot (inclusive) to the 4th spot (non-inclusive) and places them in a list [1]
print(numbers[3:4])
# Produces a boolean value after checking if the number 5 is in the list (True)
print(5 in numbers)
# Produces a boolean value after checking if the number 7 is in the list (False)
print(7 in numbers)
# Produces a boolean value if the string "3" is in the list (False)
print("3" in numbers)
# Adds the additional 3 numbers onto the list
print(numbers + [6, 5, 3])

# Question One
numbers[0] = "ten"
print(numbers)

# Question Two
numbers[-1] = 1
print(numbers)

# Question Three
print(numbers[2:])

# Question Four
print(9 in numbers)
