import os
import unittest
from wordfilter import Wordfilter


class wordfilterTest(unittest.TestCase):

    def setUp(self):
        self.wf = Wordfilter()

    def test_detects_bad_words_in_a_string(self):
        self.assertTrue(isinstance(self.wf, object))

        self.assertTrue(self.wf.blacklisted('this string contains the word skank'))
        self.assertTrue(self.wf.blacklisted('this string contains the word SkAnK'))

        self.assertFalse(self.wf.blacklisted('this string is clean!'))

    def test_add_a_word_to_blacklist(self):
        self.wf.add_words(['clean'])

        self.assertTrue(self.wf.blacklisted('this string was clean!'))

    def test_clear_blacklist(self):
        self.wf.clear_list()

        self.assertFalse(self.wf.blacklisted('this string contains the word skank'))

        self.wf.add_words(['skank'])
        self.assertTrue(self.wf.blacklisted('this string contains the word skank'))

    def test_passed_list(self):
        '''Try to add a custom list'''

        blacklist_wordfilter = Wordfilter(blacklist=['custom', 'word', 'list'])

        self.assertTrue(blacklist_wordfilter.blacklisted('custom'))
        self.assertFalse(blacklist_wordfilter.blacklisted('skank'))

    def test_custom_blacklist(self):
        '''Try to pass a txt file'''
        txt = 'dummy.txt'

        with open(txt, 'w') as f:
            f.write(u"custom\nword\nlist")

        datafile_wordfilter = Wordfilter(datafile=txt)

        self.assertTrue(datafile_wordfilter.blacklisted('custom'))
        self.assertFalse(datafile_wordfilter.blacklisted('skank'))

        os.remove(txt)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
