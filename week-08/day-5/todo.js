'use strict';
var textInput = document.querySelector('#textInput');
var addButton = document.querySelector('.addButton');
var divContainer = document.querySelector('.divContainer');

function getTodos() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var data = JSON.parse(xhr.responseText);
    data.forEach(function (e, i) {
      console.log(e);
      var newTodo = document.createElement('div');
      newTodo.classList.add("todo-item");
      newTodo.innerHTML = '<div class="task">' + data[i].text + '</div><button id = "d1" class="delButton"></button><button id = "chk1" class="chkButton"></button>';
      newTodo.setAttribute('data-id', data[i].id);
      divContainer.appendChild(newTodo);
    })
  };
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.send();
}

function addNewTodo() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var data = JSON.parse(xhr.responseText);
    var newTodo = document.createElement('div');
    newTodo.classList.add("todo-item");
    newTodo.innerHTML = '<div class="task">' + data.text + '</div><button id = "d1" class="delButton"></button><button id = "chk1" class="chkButton"></button>';
    newTodo.setAttribute('data-id', data.id);
    divContainer.appendChild(newTodo);
  };
  var newTodoToAdd = {
    text: textInput.value
  };
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify(newTodoToAdd));
}

getTodos();
addButton.addEventListener('click', addNewTodo);
