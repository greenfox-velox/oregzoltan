'use strict';

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error
var fs = require('fs');

function concatContent(fileName1, fileName2, content) {
  fs.readFile(fileName1, function(err, content1) {
    if (err) {
      return content(err);
    }
    fs.readFile(fileName2, function(err, content2) {
      if (err) {
        return content(err);
      }
      var concatContant = String(content1) + String(content2);
      content(null, concatContant);
    });
  });
}

concatContent('test1.txt', 'test2.txt', function(err, content) {
  console.log(err, content);
});
