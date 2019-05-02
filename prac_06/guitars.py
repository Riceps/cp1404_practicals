"""Client code to use the guitar class"""

from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    guitar_name = str(input("Name: "))
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))

        guitar_to_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append([guitar_name, guitar_year, guitar_cost])
        print("{} ({}) : ${} added.".format(guitar_name, guitar_year, guitar_cost))
        guitar_name = str(input("Name: "))

    i = 1
    for guitar in guitars:
        print("Guitar {}: {} ({}), worth $ {}".format(i, guitar[0], guitar[1], guitar[2]))
        i += 1


main()
