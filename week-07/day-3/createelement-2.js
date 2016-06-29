
    // Remove the king from the list.
var asteroids = document.querySelector('ul');
asteroids.removeChild(document.querySelector('li'));

    // Add 3 list items saying 'The Fox' to the list.

for (var i = 0; i < 3; i++) {
  var newItem = document.createElement('li');
  newItem.textContent = 'The Fox';
  asteroids.appendChild(newItem);
}
