import pyrebase # pip install pyrebase4
import requests
import re
import json
'''
Firebase file functions

 processHttpError(e): Process HTTP error. Returns None.

 authenticate_user(user): Authenticate user with email and password. 
 Returns True if authentication is successful, False otherwise.

 signup(): Sign up a new user. 
 Returns user's authentication token and other details.

 signin(): Sign in an existing user. 
 Returns user's authentication token and other details.

 emailVerified(user): Check if user's email is verified. 
 Returns True if email is verified, False otherwise.

 setUsername(user, name): Add or set user's Username to database. Returns None.

 setName(user, name): Add or set user's name to database. Returns None.
 
 setPronouns(user, pronouns): Add or set user's pronouns to database. Returns None.

 setMajor(user, major): Add or set user's major to database. Returns None.

 setBio(user, bio): Add or set user's bio to database. Returns None.

 setEmail(user): Add or set user's email to database. Returns None.

 setSignupInfo(user, name, email): Add or set user's username and email to database. Returns None.

 setUserInfo(user, name, pronouns, major, bio): Add or set user's name, pronouns, major, and bio to database. Returns None.
'''
 

firebaseConfig = {
  "apiKey": "AIzaSyB4rExDPr6uXlR5jrBp_5KmUVanP9wIV8w",
  "authDomain": "let-s-lunch.firebaseapp.com",
  "databaseURL": "https://let-s-lunch-default-rtdb.firebaseio.com",
  "projectId": "let-s-lunch",
  "storageBucket": "let-s-lunch.appspot.com",
  "messagingSenderId": "225888613724",
  "appId": "1:225888613724:web:512571fa2732bf704b7d99",
  "measurementId": "G-1H9J2LH6SV"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()

def processHttpError(e):
    """
    Process HTTP error.

    Args:
        e (requests.HTTPError): HTTP error.

    Returns:
        None
    """
    error_json = e.args[1]
    error = json.loads(error_json)['error']
    print("Error:", error['message'])

    #IS_INVALID_EMAIL: If the email address is malformed.
    #EMAIL_NOT_FOUND: If there is no user corresponding to the email address.
    #INVALID_PASSWORD: If the password is invalid for the given email, or the account corresponding to the email does not have a password set.
    #WEAK_PASSWORD : If the password is not strong enough.
    #EMAIL_EXISTS: If the email address already exists in the database.
    #TOO_MANY_ATTEMPTS_TRY_LATER: If there was too many attempts to sign in as this user.
    #USER_DISABLED: If the user account has been disabled by an administrator.
    #INVALID_CREDENTIALS: If the user's credentials are invalid.

    return None

def authenticate_user(user):
    """
    Authenticate user with email and password.

    Args:
        email (str): User's email address.
        password (str): User's password.

    Returns:
        True if authentication is successful, False otherwise.
    """
    try:
        auth.send_email_verification(user['idToken'])
        return True
    except requests.HTTPError as e:
        processHttpError(e)
        return False

def signup(email, password):
    """
    Sign up a new user.

    Returns:
        dict: User's authentication token and other details.
        None: If signup fails.
    """
    try:

        # Check if email ends with @gmu.edu
        """
        if not re.match(r"[^@]+@gmu\.edu", email):
            print("Please use a GMU email address.")
            return None
        """ 
        user = auth.create_user_with_email_and_password(email, password)
        print("Signup successful, verify your email to use app.")
        authenticate_user(user)
        return user
    except requests.HTTPError as e:
        return processHttpError(e)

def signin(email, password):
    """
    Sign in an existing user.

    Returns:
        dict: User's authentication token and other details.
        None: If signin fails.
    """
    try:   
        user = auth.sign_in_with_email_and_password(email, password)
        print("Signin successful!")
        return user
    except requests.HTTPError as e:
        return processHttpError(e)

def emailVerified(user):
    """
    Check if user's email is verified.

    Args:
        user (dict): User's authentication token and other details.

    Returns:
        bool: True if email is verified, False otherwise.
    """
    if user is None:        
        return False
    try:
        if auth.get_account_info(user['idToken'])['users'][0]['emailVerified']:
            return True
        else:
            return False
    except requests.HTTPError as e:
        return processHttpError(e)

def setEmail(user):
    """
    Add or set user's email to database.
    """
    try:
        email = auth.get_account_info(user['idToken'])['users'][0]['email']
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        data['email'] = email
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)

def setUsername(user, name):
    """
    Add or set user's Username to database.
    """
    try:
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        data['username'] = name
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)

def setName(user, name):
    """
    Add or set user's name to database.
    """
    try:
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        data['name'] = name
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)

def setPronouns(user, pronouns):
    """
    Add or set user's pronouns to database.
    """
    try:
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        data['pronouns'] = pronouns
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)

def setMajor(user, major):
    """
    Add or set user's major to database.
    """
    try:
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        data['major'] = major
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)

def setBio(user, bio):
    """
    Add or set user's bio to database.
    """
    try:
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        data['bio'] = bio
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)

def setSignupInfo(user, name):
    """
    Add or set user's Username and email to database.
    """
    try:
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        email = auth.get_account_info(user['idToken'])['users'][0]['email']
        data['username'] = name
        data['email'] = email
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)

def setUserInfo(user, name, pronouns, major, bio):
    """
    Add or set user's name, pronouns, major, and bio to database.
    """
    try:
        data = database.child("users").child(user['localId']).get(user['idToken']).val()
        if data is None:
            data = {}
        data['name'] = name
        data['pronouns'] = pronouns
        data['major'] = major
        data['bio'] = bio
        database.child("users").child(user['localId']).set(data, user['idToken'])
    except Exception as e:
        print("Database Error", e)