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
      if test_string.find(badword) != -1:
        return True

    return False
    
  def addWords(self, words):
    self.blacklist.extend(words.lower())

  def clearList(self):
    self.blacklist = []
