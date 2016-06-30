'use strict';

    // On the click of the button,
    // Count the items in the list
    // And display the result in the result element.
var button = document.querySelector('button');
  function counter() {
    var elements = document.querySelectorAll('li');
    document.querySelector('.result').textContent = elements.length;
  }

button.addEventListener('click', counter);
