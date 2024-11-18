from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

COLOUR_NAMES = ["AliceBlue", "British Racing Green", "Cherry Blossom Pink", "Deep Saffron", "Vanilla",
                "Teal", "Pistachio", "Opal"]


class DynamicLabel(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hex_codes = COLOUR_NAMES

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.hex_codes:
            temp_label = Label(text=name)
            self.root.ids.display_names.add_widget(temp_label)


DynamicLabel().run()
