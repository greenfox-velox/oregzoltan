'use strict';

var buttonYoda = document.querySelector('.buttonYoda');
var textInput = document.querySelector('#textInput');
var h1 = document.querySelector('h1');

function action() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var data = xhr.responseText;
    h1.textContent = data;
  };
  var urlStr = 'https://yoda.p.mashape.com/yoda?sentence=' + encodeURIComponent(textInput.value);
  xhr.open('GET', urlStr);
  xhr.setRequestHeader("X-Mashape-Key", "KEjoG3sQWtmshlaiwkAEob887fgSp1pi544jsniIOqOgC9nIXm");
  xhr.send();
}

buttonYoda.addEventListener('click', action);
