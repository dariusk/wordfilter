from os import path
import json


class Wordfilter(object):

    """filter out bad words"""

    blacklist = []

    def __init__(self, blacklist=None, datafile=None):
        if isinstance(blacklist, list):
            self.blacklist = blacklist
            return

        if datafile:
            with open(datafile, 'r') as f:
                self.blacklist = f.read().splitlines()

        else:
            datafile = path.join(path.dirname(__file__), 'badwords.json')
            self.blacklist = json.load(open(datafile, 'r')).get('badwords')

    def blacklisted(self, string):
        string = string.lower().strip()
        count = sum(True for bad in self.blacklist if string.find(bad) > -1)
        return bool(count)

    def add_words(self, lis):
        self.blacklist = self.blacklist + lis

    def clear_list(self):
        self.blacklist = []
