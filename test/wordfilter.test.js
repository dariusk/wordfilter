// See https://jshint.com/docs/ for test documentation.

// Inline configuration for jshint to ignore the undefined Jest functions:
/* globals test, expect */

var wordfilter = require('../lib/wordfilter.js');

test('detects bad words in a string', function() {
  expect(typeof(wordfilter)).toEqual('object');
  expect(wordfilter.blacklisted('this string contains the word skank')).toBeTruthy();
  expect(wordfilter.blacklisted('this string contains the word SkAnK')).toBeTruthy();
  expect(wordfilter.blacklisted('this string contains the wordskank')).toBeTruthy();
  expect(wordfilter.blacklisted('this string contains the skankword')).toBeTruthy();
  expect(wordfilter.blacklisted('this string is clean!')).toBeFalsy();
});

test('add a word to blacklist', function() {
  wordfilter.addWords(['clean']);

  expect(wordfilter.blacklisted('this string was clean!')).toBeTruthy();
});

test('remove a single word from blacklist', function() {
  wordfilter.removeWord('crip');

  expect(wordfilter.blacklisted('I have a prescription.')).toBeFalsy();
});

test('clear blacklist', function() {
  wordfilter.clearList();

  expect(wordfilter.blacklisted('this string contains the word skank')).toBeFalsy();

  wordfilter.addWords(['skank']);

  expect(wordfilter.blacklisted('this string contains the word skank')).toBeTruthy();
});
