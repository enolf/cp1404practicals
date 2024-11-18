"""
CP1404 - prac_08 - Florian N Eisen
GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder

KM_TO_MILES = 1.60934


class ConvertMilesToKilometres(App):
    """Main Program - convert miles to kilometres"""

    def build(self):
        """Build the app"""
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_m_input(self):
        """Handle user input of miles"""
        input_m = self.root.ids.input_m.text
        input_m = self.verify_float(input_m)
        output_miles = float(input_m) * KM_TO_MILES
        self.root.ids.output_km.text = f'{output_miles} miles'

    def toggle_input(self, amount):
        """Toggle the user input but +1/-1"""
        input_m = self.root.ids.input_m.text
        input_m = self.verify_float(input_m)
        input_m += amount
        self.root.ids.input_m.text = str(input_m)
        self.handle_m_input()

    def verify_float(self, input_m):
        """Verify the input is a float type"""
        try:
            float(input_m)
            return float(input_m)
        except ValueError or TypeError:
            self.root.ids.input_m.text = '0'
            return 0


ConvertMilesToKilometres().run()
