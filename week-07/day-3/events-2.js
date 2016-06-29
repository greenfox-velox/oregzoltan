// <!DOCTYPE html>
// <html lang="en">
// <head>
//   <meta charset="UTF-8">
//   <title>Workshop: EventListeners</title>
// </head>
// <body>
//   <ul>
//     <li>apple</li>
//     <li>balloon</li>
//     <li>cat</li>
//     <li>dolphin</li>
//   </ul>
//   <button>How many items are in the list?</button>
//   <p class="result">dunno :(</p>
//
//   <script>
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
