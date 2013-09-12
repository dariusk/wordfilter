/*
 * wordfilter
 * https://github.com/dariusk/wordfilter
 *
 * Copyright (c) 2013 Darius Kazemi
 * Licensed under the MIT license.
 */

'use strict';

var fs = require('fs');
var blacklist;

try {
  var data = fs.readFileSync( __dirname + '/badwords.json', 'ascii');
  data = JSON.parse(data);
  blacklist = data.badwords;
}
catch (err) {
  console.error("There was an error opening the file:");
  console.log(err);
}

function isBlacklisted(string) {
  for (var i=0;i<blacklist.length;i++) {
    if (string.toLowerCase().indexOf(blacklist[i]) >= 0) {
      return true;
    }
  }
  return false;
}

module.exports = {
  blacklisted: function(string) {
    return isBlacklisted(string);
  }
};
