'use strict';

var button = document.querySelector('.b');
var h1 = document.querySelector('h1');
var h2 = document.querySelector('h2');

function action() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var data = JSON.parse(xhr.response);
    console.log(data.celebrations.length);
    h1.textContent = 'Today: ' + data.weekday;
    h2.textContent = 'Celebrations: ' + data.celebrations.length;
  };
  xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2016/7/06')
  xhr.send();
}

button.addEventListener('click', action);
