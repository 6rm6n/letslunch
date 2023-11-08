from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import NoTransition
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.label import Label
from user import User
from userinfo import UserInfo

class HomeScreen(Screen):
    def doesLike(self):
        pass

    def doesNot(self):
        pass

class ImageButton(ButtonBehavior, Image):
    pass

class Signup1Screen(Screen):
    pass

class Signup2Screen(Screen):
    pass

class Signup3Screen(Screen):
    pass

class Signup4Screen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AddFriendScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class CentralPage(Screen):
    pass

class ChatMessage(Label):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        self.user = None
        return GUI
    
    def change_screen(self, screen_name):
        # get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager'] # root: the main widget in the layout
        screen_manager.transition = NoTransition()  # You can change the direction to "right", "up", "down", etc.
        screen_manager.current = screen_name
        #screen_manager = self.root.ids
    
    # Initializes user signup, called by firstbioscreen
    def sign_up(self, email, username, password):
        self.user = User()
        self.user.init_SignIn(email, username, password)

    button_text_list_location = []
    button_text_list_time = []

    def pressed_location(self, button_instance):
        if button_instance.background_color == [1, 0, 0, 1]:  # If the button is red
            button_instance.background_color = [0, 1, 0, 1]
        else :
            button_instance.background_color = [1, 0, 0, 1]

        button_text = button_instance.text # text
        if(button_instance.text not in self.button_text_list_location):
            self.button_text_list_location.append(button_text)
        else :
            self.button_text_list_location.remove(button_text)
        print(f'Button location text list: {self.button_text_list_location}')

    def pressed_time(self, button_instance):
        if button_instance.background_color == [1, 0, 0, 1]:  # If the button is red
            button_instance.background_color = [0, 1, 0, 1]
        else :
            button_instance.background_color = [1, 0, 0, 1]

        button_text = button_instance.text # text
        if(button_text not in self.button_text_list_time):
            self.button_text_list_time.append(button_text)
        else :
            self.button_text_list_time.remove(button_text)

        print(f'Button time text list: {self.button_text_list_time}')
    

MainApp().run()
