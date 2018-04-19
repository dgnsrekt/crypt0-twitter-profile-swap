#!python3.6

from configparser import ConfigParser
from pathlib import Path
import logging

FILEPATH = Path(__file__)
CONFIGPATH = FILEPATH.with_suffix('.ini')

BULLISH_BANNER = FILEPATH.parent / 'bullbanner.png'
BEARISH_BANNER = FILEPATH.parent / 'bearbanner.png'

BULLISH_PROFILE = FILEPATH.parent / 'bullprofile.png'
BEARISH_PROFILE = FILEPATH.parent / 'bearprofile.png'


class Configuration:

    def __init__(self):
        self.paths = [CONFIGPATH, BULLISH_BANNER,
                      BULLISH_PROFILE, BEARISH_BANNER, BEARISH_PROFILE]
        self.checkFileSystem()
        self.banner = dict()
        self.profile = dict()

        self.banner['bullish'] = str(BULLISH_BANNER.absolute())
        self.banner['bearish'] = str(BEARISH_BANNER.absolute())

        self.profile['bullish'] = str(BULLISH_PROFILE.absolute())
        self.profile['bearish'] = str(BEARISH_PROFILE.absolute())

        self.twitter = self.twitterConfig()

    def checkFileSystem(self):
        logging.debug('Checking if all files are present.')
        for _file in self.paths:
            if not _file.exists():
                if _file == CONFIGPATH:
                    print(_file)
                    self.createConfigFile()
                else:
                    raise Exception(
                        'Missing {} file. Create one.'.format(_file))

    @staticmethod
    def createConfigFile():
        config = ConfigParser()
        if not CONFIGPATH.exists():
            config['TWITTER_KEYS'] = {'CONSUMER_KEY': '',
                                      'CONSUMER_SECRET': '',
                                      'ACCESS_TOKEN': '',
                                      'ACCESS_SECRET': ''}
            with open(CONFIGPATH, 'w') as configfile:
                config.write(configfile)
                logging.info('Creating {}'.format(CONFIGPATH))
                raise Exception(
                    'Created Config file. Please fill in tokens. {}'.format(CONFIGPATH))

    @classmethod
    def twitterConfig(self):
        config = ConfigParser()
        config.read(CONFIGPATH)
        twitter_keys = dict(config['TWITTER_KEYS'])

        for key in twitter_keys:
            if not twitter_keys.get(key):
                raise Exception('Add {} to the {} file.'.format(
                    key.title(), CONFIGPATH))

        return twitter_keys
