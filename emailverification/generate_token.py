import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

# Set up the OAuth2 flow
flow = InstalledAppFlow.from_client_config({
    "installed": {
        "client_id": "883853464721-mblhop2e6np4th1ulslh0uo4q0pfi8q0.apps.googleusercontent.com",
        "client_secret": "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",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"]
    }
}, scopes=["https://www.googleapis.com/auth/gmail.send"])

# Run the OAuth2 flow
credentials = flow.run_local_server()

# Save the credentials for later use
with open("token.pkl", "wb") as token_file:
    pickle.dump(credentials, token_file)
