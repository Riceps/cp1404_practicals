# Set an upper and lower limit
UPPER_BOUNDARY = 100
LOWER_BOUNDARY = 0


def main():
    """Convert Score to grade"""
    # Receive a score between 0 and 100 inclusive from the user
    score = float(input("Enter score: "))
    # Print grade
    print(score_to_grade(score))


def score_to_grade(score):
    """Error check and return grade as string"""
    # Check which grade was received
    if UPPER_BOUNDARY < score or score < LOWER_BOUNDARY:
        return "invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
