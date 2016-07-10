'use strict';

// create a function that takes 3 parameters
//  - readFileName: a filename where it reads from
//  - wirteFileName: a filename where it writes to
//  - cb: callback with one parameter: the error if occured
//
// It should read the file named readFileName and double the text of the file
// like: "apple" -> "appleapple"
// Than it should write this doubled text to the file named writeFileName
// When it finished it should call the callback with a null
// If there is any error during the process it should call the callback with the error

var fs = require('fs');

function doubleIt(fimeNameRd, fileNameWr, cb) {
  fs.readFile(fimeNameRd, function(err, content) {
    if (err) {
      return cb(err);
    }
    var textArray = [];
    var textToWrite = '';
    String(content).replace(/\r?\n|\r/g,' ').split(' ').forEach(function(e) {
      textArray.push(e+e);
    });
    textToWrite = textArray.join(' ');
    fs.writeFile(fileNameWr, textToWrite, function(err) {
      if (err) {
        return cb(err);
      }
      cb(null);
    });
  });
}

doubleIt('test.txt', 'testtowrite.txt', function(err) {
  console.log(err);
});
