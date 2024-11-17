"""
CP1404 - prac_08 - Florian N Eisen
GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


class ConvertMilesFromKilometres(App):

    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_kilometres.kv')
