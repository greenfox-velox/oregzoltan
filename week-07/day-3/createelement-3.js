    // Remove the king from the list.

var asteroids = document.querySelector('ul');
asteroids.removeChild(document.querySelector('li'));


    // Add list items that have the following text contents:
    // ['apple', 'bubble', 'cat', 'green fox']

var listItems = ['apple', 'bubble', 'cat', 'green fox'];
for (var i = 0; i < listItems.length; i++) {
  var newItem = document.createElement('li');
  newItem.textContent = listItems[i];
  asteroids.appendChild(newItem);
}
