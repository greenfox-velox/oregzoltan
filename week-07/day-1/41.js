'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function
function sum_numbers(numbers) {
  var total = 0;
  for (var i = 0; i < numbers.length; i++) {
    total += numbers[i];
  }
  return total;
}

console.log(sum_numbers(numbers));
