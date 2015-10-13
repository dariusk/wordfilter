# wordfilter

A small module meant for use in text generators. It lets you filter strings for bad words.

## Getting Started
Install the module with: `npm install wordfilter`

```javascript
var wordfilter = require('wordfilter');
wordfilter.blacklisted('does this string have a bad word in it?'); // "false"

// clear the list entirely
wordfilter.clearList();

// add new words
wordfilter.addWords(['zebra','elephant']);
wordfilter.blacklisted('this string has zebra in it'); // "true"

// remove a word
wordfilter.removeWord('zebra');
wordfilter.blacklisted('this string has zebra in it'); // "false"
```

Or with Python:
Install the module with: `pip install wordfilter`

```python
from wordfilter import Wordfilter
wordfilter = Wordfilter()
wordfilter.blacklisted('does this string have a bad word in it?')  # False

# clear the list entirely
wordfilter.clearList()

# add new words
wordfilter.addWords(['zebra','elephant'])
wordfilter.blacklisted('this string has zebra in it')  # True
```

## Documentation
This is a word filter adapted from code that I use in a lot of my twitter bots. It is based on [a list of words that I've hand-picked](https://github.com/dariusk/wordfilter/blob/master/lib/badwords.json) for exclusion from my bots: essentially, it's a list of things that I would not say myself. Generally speaking, they are "words of oppression", aka racist/sexist/ableist things that I would not say.

The list is not all-inclusive, and I'm always adding words to it. If you'd like to file an issue or a pull request to add more words, please do so, but understand that this is primarily for use in my own projects, and I may not agree to add certain words. (For example, I have no problem with scatological words, so "shit" and "fuck" will never be on this list.)

Words are case insensitive.

Also note that due to the complexities of the English language, I am considering anything containing the substring of a bad word to be blacklisted. For example, even though "homogenous" is not a bad word, it contains the substring "homo" and it gets filtered. The reason for this is that new slang pops up all the time using compound words and I can't possibly keep up with it. I'm willing to lose a few words like "homogenous" and "Pakistan" in order to avoid false negatives.

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Lint and test your code using [Grunt](http://gruntjs.com/).

## License
Copyright (c) 2013 Darius Kazemi
Licensed under the MIT license.
