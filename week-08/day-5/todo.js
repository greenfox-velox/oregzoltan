'use strict';
var textInput = document.querySelector('#textInput');
var addButton = document.querySelector('.addButton');
var divContainer = document.querySelector('.divContainer');

function getTodos() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var data = JSON.parse(xhr.responseText);
    data.forEach(function (e, i) {
      var newTodo = document.createElement('div');
      newTodo.classList.add("todo-item");
      newTodo.innerHTML = '<div class="task">' + data[i].text + '</div><button id = "d' + data[i].id + '" class="delButton"></button><button id = "chk' + data[i].id + '" class="chkButton"></button>';
      newTodo.setAttribute('id', 'di'+data[i].id);
      divContainer.appendChild(newTodo);
      document.getElementById('d'+data[i].id).addEventListener('click', delTodo);
      document.getElementById('chk'+data[i].id).addEventListener('click', chkTodo);
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
    newTodo.innerHTML = '<div class="task">' + data.text + '</div><button id = "d' + data.id + '" class="delButton"></button><button id = "chk' + data.id + '" class="chkButton"></button>';
    newTodo.setAttribute('id', 'di'+data.id);
    divContainer.appendChild(newTodo);
    document.getElementById('d'+data.id).addEventListener('click', delTodo);
    document.getElementById('chk'+data.id).addEventListener('click', chkTodo);

  };
  var newTodoToAdd = {
    text: textInput.value
  };
  textInput.value ='';
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify(newTodoToAdd));
}

function delTodo(event) {
  var xhr = new XMLHttpRequest();
  var id = event.target.getAttribute('id').slice(1);
  xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.send(null);
  divContainer.removeChild(document.getElementById('di'+id));
}

function chkTodo(event) {
  var xhr = new XMLHttpRequest();
  var id = event.target.getAttribute('id').slice(3);
  var toSend = {
    text: document.querySelector('#di'+id + ' div').textContent,
    completed: true
  };
  console.log(toSend);
  xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.send(toSend);
}

getTodos();
addButton.addEventListener('click', addNewTodo);
