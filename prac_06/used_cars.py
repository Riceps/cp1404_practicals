"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100, "Limo")  # Add a car object with 100 units of fuel
    limo.add_fuel(20)  # Add 20 more units of fuel to the new car
    print("Limo fuel = {}".format(limo.fuel))  # Print the amount of fuel in the limo
    limo.drive(115)  # Drive limo 115 km
    print("Limo odo = {}".format(limo.odometer))  # Print the odometer of the limo
    print(limo)

    my_car = Car(180, "Beast Wagon")
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()
