# create account / sign up thing
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import smtplib
import re
from userinfo import UserInfo
from user import User
import smtplib
import base64
from google.oauth2.credentials import Credentials
import google.auth.transport.requests

class SignupScreen(Screen):

    """def sign_up(self, email, username, password):
        # Check if email ends with @gmu.edu
        if not re.match(r"[^@]+@gmu\.edu", email):
            self.message = "Please enter a valid GMU email."
            return

        # Check username and password length as a basic validation
        if len(username) < 4:
            self.message = "Username should be at least 4 characters."
            return

        if len(password) < 6:
            self.message = "Password should be at least 6 characters."
            print(self.message)
            return
        """
    def build(self):
        return SignupScreen()
