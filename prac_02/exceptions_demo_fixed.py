"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_number = False
while not valid_number:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Invalid input, denominator must be non-zero integer")
        else:
            fraction = numerator / denominator
            print(fraction)
            valid_number = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. A value error will occur when the user inputs a value that is NOT an integer for the num or den.
# 2. A Zero division error will occur if the user inputs a "0" for the denominator value.
# 3. Yes
