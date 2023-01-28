import tweepy

CONSUMER_KEY = "tEnKUdiIeUdtCBDIlqgiRytnB"
CONSUMER_SECRET = "rKWGHjPz8wTMJJxWENoOM1KCAcvBsdj8F0yz1kVkDLTUW2ZCX3"
ACCESS_TOKEN = '1619144764749713408-neXtNGLrrpoDClfvJavSrrZDUzk3bY'
ACCESS_TOKEN_SECRET = "qoFqNGH997o9gwLUwVVd3VrNPKn3tRA7BIPtBiIl8WJFK"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)  

# Check credentials
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

# Create a tweet
api.update_status("Coca cola")

