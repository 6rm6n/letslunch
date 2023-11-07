from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import NoTransition
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.label import Label
from user import User
from userinfo import UserInfo
import signup
import dbGetter


class HomeScreen(Screen):
    def doesLike(self):
        pass

    def doesNot(self):
        pass

class ImageButton(ButtonBehavior, Image):
    pass

class SignupScreen(Screen):
    pass

class FirstBioScreen(Screen):
    pass

class SecondBioScreen(Screen):
    pass

class ThirdBioScreen(Screen):
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

class BioValidation(Screen):
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

MainApp().run()
