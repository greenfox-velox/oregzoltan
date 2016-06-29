// fill every paragraph with the last one's content.
var elements = document.querySelectorAll('p');
for (var i = 0; i < elements.length; i++) {
  elements[i].innerHTML = document.querySelector(':nth-child(4)').innerHTML;
}
