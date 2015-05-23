/*
 * wordfilter
 * https://github.com/dariusk/wordfilter
 *
 * Copyright (c) 2013 Darius Kazemi
 * Licensed under the MIT license.
 */

'use strict';

var blacklist, regex;

function rebuild() {
  regex = new RegExp(blacklist.join('|'), 'i');
}

blacklist = require('./badwords.json');
rebuild();

module.exports = {
  blacklisted: function(string) {
    return !!blacklist.length && regex.test(string);
  },
  addWords: function(array) {
    blacklist = blacklist.concat(array);
    rebuild();
  },
  removeWord: function(word) {
    var index = blacklist.indexOf(word);
    if (index > -1) {
      blacklist.splice(index, 1);
      rebuild();
    }
  },
  clearList: function() {
    blacklist = [];
    rebuild();
  },
};
