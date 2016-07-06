'use strict';
const isSudokuValid = require('./dojo2');
const test = require('tape');
var fourTimesFourList = [
  [1, 2, 3, 4],
  [4, 3, 2, 1],
  [2, 1, 4, 3],
  [3, 4, 1, 2]]

var invalidFourTimesFourList = [
  [1, 3, 2, 4],
  [4, 3, 2, 1],
  [2, 1, 4, 3],
  [3, 4, 1, 2]]

test('test lines number', function (t) {
  t.equal(isSudokuValid(fourTimesFourList), true);
  t.end();
});

test('test for invalid row ', function (t) {
  t.equal(isSudokuValid(invalidFourTimesFourList), false);
  t.end();
});

test('test for two invalid column', function (t) {
  t.equal(isSudokuValid(invalidFourTimesFourList), false);
  t.end();
});
