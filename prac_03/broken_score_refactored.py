"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
"Set an upper and lower limit"
upper_boundary = 100
lower_boundary = 0
"receive a score between 0 and 100 inclusive from the user"
score = float(input("Enter score: "))


if lower_boundary <= score <= upper_boundary:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")
else:
    print("Invalid score")

"NO ERROR CHECKING WAS IMPLEMENTED TO ENSURE NO STRINGS WERE ENTERED (OUTSIDE SCOPE OF ASSESSMENT?)"

'''if 90 <= score <= 100:
    print("Excellent")
elif score >= 50:
    print("Pass")
elif score < 50:
    print("Bad")
else:
    print("Invalid score")'''
