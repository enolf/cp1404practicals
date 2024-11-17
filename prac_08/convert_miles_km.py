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
        try:
            output_miles = float(input_km) * KM_TO_MILES
            self.root.ids.output_miles.text = str(output_miles)
        except ValueError or TypeError:
            pass


ConvertMilesFromKilometres().run()
