def main():
    """
    CP1404/CP5632 - Practical
    Pseudocode for temperature conversion
    """

    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            # Ask user for a celsius temperature
            fahrenheit = convert_to_fahrenheit(float(input("Celsius: ")))
            # Print the results from the convert to fahrenheit function
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # "Ask user for a fahrenheit temperature"
            celsius = convert_to_celsius(float(input("Fahrenheit: ")))
            # "Print the results from the convert to celsius function
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


main()
