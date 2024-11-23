"""
CP1404 - prac_08 - Florian Eisen
Demonstration of using Kivy Box Layout
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main Program - Kivy app for demonstrating box layout UI"""
    def build(self):
        """Build the app"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle press of 'greet' button"""
        name_input = self.root.ids.input_name.text
        self.root.ids.output_label.text = f'Greetings {name_input}'

    def handle_clear(self):
        """Handle press of 'clear' button"""
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
