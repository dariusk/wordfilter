'use strict';

var wordfilter = require('../lib/wordfilter.js');

/*
  ======== A Handy Little Nodeunit Reference ========
  https://github.com/caolan/nodeunit

  Test methods:
    test.expect(numAssertions)
    test.done()
  Test assertions:
    test.ok(value, [message])
    test.equal(actual, expected, [message])
    test.notEqual(actual, expected, [message])
    test.deepEqual(actual, expected, [message])
    test.notDeepEqual(actual, expected, [message])
    test.strictEqual(actual, expected, [message])
    test.notStrictEqual(actual, expected, [message])
    test.throws(block, [error], [message])
    test.doesNotThrow(block, [error], [message])
    test.ifError(value)
*/

exports['awesome'] = {
  setUp: function(done) {
    // setup here
    done();
  },
  'detects bad words in a string': function(test) {
    test.expect(6);
    // tests here
    test.equal(typeof(wordfilter), 'object', 'should return an object');
    test.equal(wordfilter.blacklisted('this string contains the word skank'), true, 'skank should be true');
    test.equal(wordfilter.blacklisted('this string contains the word SkAnK'), true, 'SkAnK should be true');
    test.equal(wordfilter.blacklisted('this string contains the wordskank'), true, 'wordskank should be true');
    test.equal(wordfilter.blacklisted('this string contains the skankword'), true, 'skankword should be true');
    test.equal(wordfilter.blacklisted('this string is clean!'), false, 'should be false');
    test.done();
  },
  'add a word to blacklist': function(test) {
    wordfilter.addWords(['clean']);

    test.expect(1);
    test.equal(wordfilter.blacklisted('this string was clean!'), true, 'should be true');
    test.done();
  },
  'remove a single word from blacklist': function(test) {
    wordfilter.removeWord('crip');

    test.expect(1);
    test.equal(wordfilter.blacklisted('I have a prescription.'), false, 'should be false');
    test.done();
  },
  'clear blacklist': function(test) {
    wordfilter.clearList();

    test.expect(2);
    test.equal(wordfilter.blacklisted('this string contains the word skank'), false, 'list is now empty so false');

    wordfilter.addWords(['skank']);
    test.equal(wordfilter.blacklisted('this string contains the word skank'), true, 'skank was re-added so true');

    test.done();
  }
};
