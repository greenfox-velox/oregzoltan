'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(a, b) {
  this.a = a;
  this.b = b;
}

Rectangle.prototype.getArea = function() {
  return this.a * this.b;
};

Rectangle.prototype.getCircumference = function() {
  return 2 * (this.a + this.b);
};

var rec = new Rectangle(3, 5);
console.log(rec.getArea());
console.log(rec.getCircumference());


module.exports.Rectangle = Rectangle;
