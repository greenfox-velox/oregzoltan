'use strict';

const createNewTodo = require('./todos');
const test = require('tape');

test('test empty text', function (t) {
  t.deepEqual(createNewTodo(1, ''), {'id': 1, 'text': '', 'completed': false});
  t.end();
});

test('is completed false', function (t) {
  t.notDeepEqual(createNewTodo(2, 'do sport'), {'id': 2, 'text': 'do sport', 'completed': true});
  t.end();
});

test('is id a number', function (t) {
  t.notDeepEqual(createNewTodo(3, 'hey'), {'id': 'a', 'text': 'hey', 'completed': false});
  t.end();
});

test('is text correct', function (t) {
  t.notDeepEqual(createNewTodo(4, 'hey'), {'id': 'a', 'text': 'heyy', 'completed': false});
  t.end();
});

test('is output an object', function (t) {
  t.notDeepEqual(createNewTodo(5, 'yes'), [{'id': '5', 'text': 'yes', 'completed': false}]);
  t.end();
});
