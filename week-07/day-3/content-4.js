    // replace the list items' content with items from this list:
    // ['apple', 'banana', 'cat', 'dog']

var elements = document.querySelectorAll('li');
var words = ['apple', 'banana', 'cat', 'dog'];

for (var i = 0; i < elements.length; i++) {
  elements[i].textContent = words[i];
}
