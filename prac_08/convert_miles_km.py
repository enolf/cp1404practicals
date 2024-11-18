"""
CP1404 - prac_08 - Florian N Eisen
GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder

KM_TO_MILES = 1.60934


class ConvertMilesFromKilometres(App):

    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_km_input(self):
        input_km = self.root.ids.input_km.text
        input_km = self.verify_float(input_km)
        output_miles = float(input_km) * KM_TO_MILES
        self.root.ids.output_miles.text = str(output_miles)

    def toggle_input(self, amount):
        input_km = self.root.ids.input_km.text
        input_km = self.verify_float(input_km)
        input_km += amount
        self.root.ids.input_km.text = str(input_km)
        self.handle_km_input()

    def verify_float(self, input_km):
        try:
            float(input_km)
            return float(input_km)
        except ValueError or TypeError:
            return 0


ConvertMilesFromKilometres().run()
