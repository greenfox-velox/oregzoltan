'use strict';

const isSudokuLineValid = require('./dojo');
const test = require('tape');

test('test empty line', function (t) {
  t.equal(isSudokuLineValid([]), false);
  t.end();
});

test('test for nine elements', function (t) {
  t.equal(isSudokuLineValid([1, 2, 3, 4, 5, 6, 7, 8, 9]
  ), true);
  t.end();
});

test('test for duplicate elements', function (t) {
  t.equal(isSudokuLineValid([1, 2, 3, 3, 5, 6, 7, 8, 8]
  ), false);
  t.end();
});

test('test for line with letter', function (t) {
  t.equal(isSudokuLineValid([1, 2, 3, 4, 5, 'g', 7, 8, 9]
  ), false);
  t.end();
});

test('test for nonOrdered list', function (t) {
  t.equal(isSudokuLineValid([1, 2, 3, 5, 4, 9, 7, 8, 6]
  ), true);
  t.end();
});

test('test for duplicate', function(t) {
  t.equal(isSudokuLineValid([1, 2, 3, 5, 4, 7, 2, 9, 6]
  ), false);
  t.end();
})

test('test for valid line length', function(t) {
  t.equal(isSudokuLineValid([1, 2, 3, 5, 4, 7, 8, 9, 6, 10, 11, 12, 13, 14, 15]
  ), false);
  t.end();
})

module.exports = isSudokuValid;
