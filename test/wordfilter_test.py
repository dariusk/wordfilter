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
        assert self.wordfilter.blacklisted(
            'this string contains the word skank')
        assert self.wordfilter.blacklisted(
            'this string contains the word SkAnK')
        assert self.wordfilter.blacklisted(
            'this string contains the wordskank')
        assert self.wordfilter.blacklisted(
            'this string contains the skankword')
        assert not self.wordfilter.blacklisted('this string is clean!')

    def test_addWords(self):
        self.wordfilter.addWords(['clean'])
        assert self.wordfilter.blacklisted(
            'this string contains the word skank')
        assert self.wordfilter.blacklisted('this string is clean!')

    def test_removeWord(self):
        # Act
        self.wordfilter.removeWord('crip')

        # Assert
        assert not self.wordfilter.blacklisted('I have a prescription.')

    def test_remove_multiple_added_words(self):
        # Arrange
        # Add several to make sure all instances are removed:
        self.wordfilter.addWords(['crip', 'crip'])

        # Act
        self.wordfilter.removeWord('crip')

        # Assert
        assert not self.wordfilter.blacklisted('I have a prescription.')

    def test_remove_unblacklisted_word(self):
        # Arrange
        # Make sure no error when removing a word that's not on the list
        assert not self.wordfilter.blacklisted('this string is clean!')

        # Act
        self.wordfilter.removeWord('clean')

        # Assert
        assert not self.wordfilter.blacklisted('this string is clean!')

    def test_clearList(self):
        self.wordfilter.clearList()
        assert not self.wordfilter.blacklisted(
            'this string contains the word skank')

        self.wordfilter.addWords(['skank'])
        assert self.wordfilter.blacklisted(
            'this string contains the word skank')

    def test_add_multiple_words(self):
        # Arrange
        self.wordfilter.clearList()

        # Act
        self.wordfilter.addWords(['zebra', 'elephant'])

        # Assert
        assert self.wordfilter.blacklisted('this string has zebra in it')
        assert self.wordfilter.blacklisted('this string has elephant in it')
        assert not self.wordfilter.blacklisted('this string has nothing in it')

if __name__ == "__main__":
    nose.main()
