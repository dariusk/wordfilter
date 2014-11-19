/*
 * wordfilter
 * https://github.com/dariusk/wordfilter
 *
 * Copyright (c) 2013 Darius Kazemi
 * Licensed under the MIT license.
 */

'use strict';

var fs = require('fs');
var blacklist, regex;

function rebuild() {
  regex = new RegExp(blacklist.join('|'), 'i');
}

try {
  var data = fs.readFileSync( __dirname + '/badwords.json', 'ascii');
  data = JSON.parse(data);
  blacklist = data.badwords;
  rebuild();
}
catch (err) {
  console.error("There was an error opening the file:");
  console.log(err);
}

module.exports = {
  blacklisted: function(string) {
    return !!blacklist.length && regex.test(string);
  },
  addWords: function(array) {
    blacklist = blacklist.concat(array);
    rebuild();
  },
  clearList: function() {
    blacklist = [];
    rebuild();
  }
};
