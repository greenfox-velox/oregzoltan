'use strict';

function isInt(element) {
  return typeof element === 'number';
}

function isUnique(element, index) {
  return element === index + 1;
}

function compareNumbers(a, b) {
  return a - b;
}

function isSquared(linelist) {
  return Math.sqrt(linelist.length) % 1 === 0;
}

function isValidValues(linelist) {
  return linelist.sort(compareNumbers).every(isUnique) && linelist.every(isInt);
}

function isSudokuLineValid(linelist) {
  if (!(linelist.length && isSquared(linelist))){
    return false;
  }
  return isValidValues(linelist);
}

module.exports = isSudokuLineValid;
