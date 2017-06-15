class Tweeter:
    def __init__(self, config, tweepy):
        self.tweepy = tweepy
        self.config = config

    def send(self, filename, status_text):

        ckey = self.config["ckey"]
        csecret = self.config["csecret"]
        akey = self.config["akey"]
        asecret = self.config["asecret"]

        auth = self.tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(akey, asecret)
        api = self.tweepy.API(auth)
        api.update_with_media(filename, status=status_text)

