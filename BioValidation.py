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
        
        self.pressed_buttons_time = []  # List to store pressed buttons time wise
        self.pressed_buttons_location = []  # List to store pressed buttons location wise

        #buttons for time
        self.noon = Button(text="Noon", font_size=40)
        self.eleven_thirty = Button(text="11:30", font_size=40)
        self.twelve_thirty = Button(text="12:30", font_size=40)

        #buttons for location
        self.southside = Button(text="Southside", font_size=40)
        self.ikes = Button(text="Ikes", font_size=40)
        self.Globe = Button(text="Globe", font_size=40)
        
        # Create an error label for validation messages
        self.error_label = Label(text='', color=(1, 0, 0, 1))

        # Create a submit button
        submit_button = Button(text='Submit', on_press=self.validate_inputs)

        #binding or collecting information from buttons time wise
        self.noon.bind(on_press=self.pressed_time)
        self.eleven_thirty.bind(on_press=self.pressed_time)
        self.twelve_thirty.bind(on_press=self.pressed_time)

        #binding or collecting information from buttons location wise
        self.southside.bind(on_press=self.pressed_location)
        self.ikes.bind(on_press=self.pressed_location)
        self.Globe.bind(on_press=self.pressed_location)

        # Add widgets to the layout
        layout.add_widget(self.name_input)
        layout.add_widget(self.error_label)

        #the buttons for the times
        layout.add_widget(self.noon)
        layout.add_widget(self.eleven_thirty)
        layout.add_widget(self.twelve_thirty)

        #the buttons for the locations
        layout.add_widget(self.southside)
        layout.add_widget(self.ikes)
        layout.add_widget(self.Globe)

        #validating what buttons are pressed
        self.label = Label(text="")

        layout.add_widget(submit_button)

        return layout

    def validate_inputs(self, instance):
        # Retrieve user input
        name = self.name_input.text.strip()

        # Check if any of the fields are empty
        if not name:
            self.error_label.text = 'Please fill in Name field.'
        else:
            # All fields are filled, display a success message (you can perform other actions here)
            self.error_label.text = f'your input is successful!'

    #button pressed or not, these are times that someone has lunch at
    def pressed_time(self, instance):
        button_text = instance.text
        if button_text not in self.pressed_buttons_time:
            self.pressed_buttons_time.append(button_text)
        print(self.pressed_buttons_time)

    #button pressed or not, these are locations that someone has lunch at
    def pressed_location(self, instance):
        button_text = instance.text
        if button_text not in self.pressed_buttons_location:
            self.pressed_buttons_location.append(button_text)
        print(self.pressed_buttons_location)

if __name__ == '__main__':
    LunchApp().run()
