"""KIVY GUI program to convert miles to kilometres"""

from kivy.app import App
from kivy.lang import Builder

# Constants
MILES_TO_KILOMETRES_RATIO = 1.609


class MileToKilometreApp(App):
    """Conversion of miles to kilometres app"""

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Mile to Kilometre"
        self.root = Builder.load_file('miles_to_kilometres_converter.kv')
        return self.root

    def handle_calculate(self):
        """Converts miles to kilometres"""
        miles = self.is_valid_distance()
        # Convert from miles to kilometres
        kilometres = miles * MILES_TO_KILOMETRES_RATIO
        self.root.ids.output_label.text = str(kilometres)

    def is_valid_distance(self):
        """Checks if input is a number, if it isn't, a zero will be returned"""
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0

    def handle_increment(self, increment):
        """Increment the current number up or down"""
        # check if the current input is valid number
        miles = self.is_valid_distance()
        # Add / subtract 1 from the number
        incremented_miles = miles + increment
        # Replace input with incremented number
        self.root.ids.input_number.text = str(incremented_miles)
        # Reevaluate the miles to kilometres with new number
        self.handle_calculate()


MileToKilometreApp().run()
