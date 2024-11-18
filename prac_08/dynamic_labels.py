"""
CP1404 - prac_08 - Florian N Eisen
Dynamic Labels created from a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

COLOUR_NAMES = ["AliceBlue", "British Racing Green", "Cherry Blossom Pink", "Deep Saffron", "Vanilla",
                "Teal", "Pistachio", "Opal"]


class DynamicLabel(App):

    def __init__(self, **kwargs):
        """Construct Main App"""
        super().__init__(**kwargs)
        self.hex_codes = COLOUR_NAMES

    def build(self):
        """Build App"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list of names"""
        for name in self.hex_codes:
            temp_label = Label(text=name)
            self.root.ids.display_names.add_widget(temp_label)


DynamicLabel().run()
