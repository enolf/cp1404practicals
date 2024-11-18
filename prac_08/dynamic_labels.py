from kivy.app import App
from kivy.lang import Builder
from kivy.uix import Button
from kivy.properties import StringProperty

NAMES_TO_HEX_CODES = {"AliceBlue": "#f0f8ff", "British Racing Green": "#004225",
                      "Cherry Blossom Pink": "#ffb7c5", "Deep Saffron": "#ff9933",
                      "Vanilla": "#f3e5ab", "Teal": "#008080", "Pistachio": "#93c572",
                      "Opal": "#a8c3bc", "LimeGreen": "#32cd32", "Key Lime": "#e8f48c"}


class DynamicLabel(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hex_codes = NAMES_TO_HEX_CODES

    def build(self):
        for name in self.hex_codes:



DynamicLabel().run()
