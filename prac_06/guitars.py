"""Client code to use the guitar class"""

from prac_06.guitar import Guitar


def main():
    """Utilise guitar class"""
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My guitars!")
    guitar_name = str(input("Name: "))
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))

        guitar_to_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_to_add)
        print("{} ({}) : ${} added.".format(guitar_name, guitar_year, guitar_cost))
        guitar_name = str(input("Name: "))

    print(guitars)
    # How do i use the class ???
    for i, guitar in enumerate(guitars, 1):
        # if guitar.is_vintage():
        print("Guitar {}: {} ({}), worth $ {}".format(i, guitar.name, guitar.year, guitar.cost))


main()
