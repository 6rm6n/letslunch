from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from userinfo import UserInfo

class User:
    def __init__(self):
        self.userInfo = None
        self.lunchCount = 0
        self.rating = 0.0
        self.ratingCount = 0 # Used to calculate the actual rating
        self.avatar = None
        self.location = None
        self.favfood = None # Icon for what the person is eating

    # Will be called when Sign up Button is pressed or in settings
    def init_SignIn(self, email, username, password):
        self.userInfo = UserInfo(email, username, password)

    #def init_UserInfo(self, name, pronouns, major, ):



    # Called when a lunch session with the user is finished
    def increaseLunchCount(self):
        self.lunchCount += 1
    
    # Calculates user rating from eating lunches
    def calculate_rating(self, num):
        
        self.rating = (self.rating * self.ratingCount) + num
        self.ratingCount += 1
        self.rating /= self.ratingCount
    
    # Maybe be used to call another function that will take input from user and do its thing
    #def rate_user():


























     
