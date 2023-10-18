from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LunchApp(App):
    def build(self):
        self.title = 'Lunch'

        # Create a layout for the input fields and error label
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create text input fields
        self.name_input = TextInput(hint_text='Enter your name', multiline=False)
        self.location_input = TextInput(hint_text='Enter preferred lunch location', multiline=False)
        self.time_input = TextInput(hint_text='Enter preferred lunch time', multiline=False)

        # Create an error label for validation messages
        self.error_label = Label(text='', color=(1, 0, 0, 1))

        # Create a submit button
        submit_button = Button(text='Submit', on_press=self.validate_inputs)

        # Add widgets to the layout
        layout.add_widget(self.name_input)
        layout.add_widget(self.location_input)
        layout.add_widget(self.time_input)
        layout.add_widget(self.error_label)
        layout.add_widget(submit_button)

        return layout

    def validate_inputs(self, instance):
        # Retrieve user input
        name = self.name_input.text.strip()
        location = self.location_input.text.strip()
        time = self.time_input.text.strip()

        # Check if any of the fields are empty
        if not name or not location or not time:
            self.error_label.text = 'Please fill in all fields.'
        else:
            # All fields are filled, display a success message (you can perform other actions here)
            self.error_label.text = f'your input is successful!'


if __name__ == '__main__':
    LunchApp().run()
