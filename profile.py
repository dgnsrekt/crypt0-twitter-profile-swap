#!python3.6

import logging as log
import tweepy
from settings import Configuration

CONFIG = Configuration()


class TwitterProfile:

    def __init__(self):
        self.twitter_keys = CONFIG.twitter

        # Consumer keys and access tokens, used for OAuth
        self.consumer_key = self.twitter_keys['consumer_key']
        self.consumer_secret = self.twitter_keys['consumer_secret']
        self.access_token = self.twitter_keys['access_token']
        self.access_token_secret = self.twitter_keys['access_token_secret']

        # OAuth process, using the keys and tokens
        self.auth = tweepy.OAuthHandler(
            self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)

        # Creation of the actual interface, using authentication
        self.api = tweepy.API(self.auth)

        # Creates the user object. The me() method returns the user whose
        # authentication keys were used.
        self.user = self.api.me()

    def setBullishProfileStatus(self):
        print('Profile set to bullish.')
        self.api.update_profile_banner(CONFIG.banner['bullish'])
        self.api.update_profile_image(CONFIG.profile['bullish'])

    def setBearishProfileStatus(self):
        print('Profile set to bearish.')
        self.api.update_profile_banner(CONFIG.banner['bearish'])
        self.api.update_profile_image(CONFIG.profile['bearish'])


def test():
    from time import sleep
    profile = TwitterProfile()
    profile.setBearishProfileStatus()
    sleep(30)
    profile.setBullishProfileStatus()


if __name__ == '__main__':
    test()
