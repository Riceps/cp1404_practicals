"""Dynamically add labels from a list"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class MyDynamicWidgetsApp(App):
    """Creates labels dynamically from a list"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Jake Rice", "Lindsay Ward"]

    def build(self):
        """Build the KIVY GUI."""
        self.title = "My Dynamic Widgets"
        self.root = Builder.load_file('my_dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list of names"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


MyDynamicWidgetsApp().run()
