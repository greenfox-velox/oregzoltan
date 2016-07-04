'use strict';

var bookCounter = require('./02');
var tape = require('tape');
var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];
var students2 = [
  {name: 'Sheela', age: 14}
];
var students3 = [
  {name: 'Sheela', age: 14, books: []}
];

tape(function(t) {
  t.deepEqual(bookCounter.bookCounter(students), 4);
  t.deepEqual(bookCounter.bookCounter(students2), 0);
  t.deepEqual(bookCounter.bookCounter(students3), 0);
  t.end();
});
