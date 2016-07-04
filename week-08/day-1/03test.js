'use strict';

var Rectangle = require('./03');
var tape = require('tape');
var rec = new Rectangle.Rectangle(3, 5);
tape(function(t) {
  t.deepEqual(rec.getArea(), 15);
  t.deepEqual(rec.getCircumference(), 16);
  t.deepEqual(rec.a, 3);
  t.deepEqual(rec.b, 5);
  t.end();
});
