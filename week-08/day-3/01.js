'use strict';

// create a function that takes a fimename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

var fs = require('fs');

function wordCount(fimeName, cb) {
  fs.readFile(fimeName, function(err, content) {
    if (err) {
      return cb(err);
    }
    var count = String(content).replace(/\r?\n|\r/g,' ').split(' ').length-1;
    cb(null, count);
  })
}

wordCount('test.txt', function(err, count) {
  console.log(err, count);
});
