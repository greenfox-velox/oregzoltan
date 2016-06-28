'use strict';

// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function is_letter_in_string(string, letter) {
  return string.indexOf(letter) !== -1
}

console.log(is_letter_in_string('kocsi','s'));

function isLetterInString(string, letter) {
 return string.split('').some(function (e) {
   return (e === letter);
 });
}

console.log(isLetterInString('kocsi','s'));
