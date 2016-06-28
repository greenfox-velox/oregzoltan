'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isAllPrime(numbers) {
  return numbers.every(function(e) {
    for (var i = 2; i < e; i++) {
        if (e % i === 0) {
        return false;
      }
    }
    return true;
  });
}

console.log(isAllPrime(numbers));
