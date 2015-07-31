import os
import json


class Wordfilter:
    def __init__(self):
        # json is in same directory as this class, given by __location__.
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, 'badwords.json')) as f:
            self.blacklist = json.loads(f.read())

    def blacklisted(self, string):
        test_string = string.lower()
        for badword in self.blacklist:
            if badword in test_string:
                return True

        return False

    def addWords(self, words):
        self.blacklist.extend([word.lower() for word in words])

    def removeWord(self, word):
        self.blacklist = [x for x in self.blacklist if x != word]

    def clearList(self):
        self.blacklist = []
