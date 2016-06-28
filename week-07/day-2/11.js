'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack() {
  this.stack = [],
  this.size = function() {
    return this.stack.length;
  },
  this.push = function(item) {
    this.stack.push(item);
  },
  this.pop = function() {
    var last = this.stack[this.stack.length-1];
    this.stack.pop();
    return last;
  }
}

var zoli = new Stack();
zoli.push('alma');
zoli.push('laptop');
console.log(zoli.size());
zoli.push('cigi');
console.log(zoli.pop());
console.log(zoli.stack);
