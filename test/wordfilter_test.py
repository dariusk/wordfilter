import nose
from lib.wordfilter import Wordfilter

# Run with `python -m test.wordfilter_test`
class Wordfilter_test:
  def setup(self):
    self.wordfilter = Wordfilter()

  def teardown(self):
    self.wordfilter = []

  def test_loading(self):
    assert type(self.wordfilter.blacklist) is list

  def test_badWords(self):
    assert self.wordfilter.blacklisted('this string contains the word skank')
    assert self.wordfilter.blacklisted('this string contains the word SkAnK')
    assert self.wordfilter.blacklisted('this string contains the wordskank')
    assert self.wordfilter.blacklisted('this string contains the skankword')
    assert not self.wordfilter.blacklisted('this string is clean!')

  def test_addWords(self):
    self.wordfilter.addWords(['clean'])
    assert self.wordfilter.blacklisted('this string contains the word skank')
    assert self.wordfilter.blacklisted('this string is clean!')

  def test_clearList(self):
    self.wordfilter.clearList();
    assert not self.wordfilter.blacklisted('this string contains the word skank')

    self.wordfilter.addWords(['skank'])
    assert self.wordfilter.blacklisted('this string contains the word skank')

if __name__ == "__main__":
  nose.main()
