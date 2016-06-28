'use strict';

// create a function that returns it's input factorial
function factorial(number) {
  var total = 1;
  for (var i = 1; i <= number; i++) {
    total *= i;
  }
  return total;
}

console.log(factorial(4));
