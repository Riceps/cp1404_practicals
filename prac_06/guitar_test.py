"""Client code to test the guitar class"""

from prac_06.guitar import Guitar


def main():
    """Test guitar class"""
    my_guitar = Guitar("Gibson", 1922, 16035.40)
    print(my_guitar)
    print("Expected 97. Got {}".format(my_guitar.get_age()))
    print("Expected True. Got {}".format(my_guitar.is_vintage()))


main()
