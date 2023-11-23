import userinfo

class User:
    def __init__(self):
        self.userInfo = None
        self.lunchCount = 0
        self.rating = 0
        self.ratingCount = 0
        self.location = None
        self.favfood = None # Icon for what the person is eating

    # Will be called when Sign up Button is pressed
    def init_SignUp(self, email, username, password):
        self.userInfo = userinfo.signup(email, password)
        userinfo.setSignupInfo(self.userInfo, username)
        
    def init_UserInfo(self, name, pronouns, major, bio):
        userinfo.setUserInfo(self.userInfo, name, pronouns, major, bio)


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


























     
