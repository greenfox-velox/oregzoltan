'use strict';
var textInput = document.querySelector('#textInput');
var addButton = document.querySelector('.addButton');
var divContainer = document.querySelector('.divContainer');
var url = 'http://localhost:3000/todos';

function createAnElement(id, dataText) {
  var newTodo = document.createElement('div');
  newTodo.classList.add("todo-item");
  newTodo.innerHTML = '<div class="task">' + dataText + '</div><button id = "yod' + id + '" class="yodaButton"></button><button id = "d' + id + '" class="delButton"></button><button id = "chk' + id + '" class="chkButton"></button>';
  newTodo.setAttribute('id', 'di'+id);
  divContainer.appendChild(newTodo);
  createButtons(id);
}

function createButtons(id) {
  document.getElementById('d'+id).addEventListener('click', delTodo);
  document.getElementById('chk'+id).addEventListener('click', chkTodo);
  document.getElementById('yod'+id).addEventListener('click', yodaTodo);
  document.getElementById('chk'+id).classList.add('unchecked');
}

function xhrRequest(method, url, data, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, url, true);
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(data);
  xhr.onload = function () {
    if (xhr.readyState === 4) {
      callback(xhr.response);
    }
  }
}

function getTodos() {
  xhrRequest('GET', url, '', function(response) {
    var data = JSON.parse(response);
    data.forEach(function (e, i) {
      createAnElement(data[i].id, data[i].text);
      if (e.completed) {
        document.getElementById('chk'+data[i].id).classList.add('checked');
      }
    })
  })
}

function addNewTodo() {
  var newTodoToAdd = {text: textInput.value};
  textInput.value ='';
  xhrRequest('POST', url, JSON.stringify(newTodoToAdd), function(response) {
    var data = JSON.parse(response);
    createAnElement(data.id, data.text);
  })
}

function delTodo(event) {
  var id = event.target.getAttribute('id').slice(1);
  xhrRequest('DELETE', url + '/' + id, '', function(response) {
    divContainer.removeChild(document.getElementById('di'+id));
  })
}

function chkTodo(event) {
  var id = event.target.getAttribute('id').slice(3);
  var toSend = {
    text: document.querySelector('#di'+id + ' div').textContent,
    completed: !document.getElementById('chk'+id).classList.contains('checked')
  };
  xhrRequest('PUT', url + '/' + id, JSON.stringify(toSend), function(response) {
    document.getElementById('chk'+id).classList.toggle('checked');
  })
}

function yodaTodo(event) {
  var id = event.target.getAttribute('id').slice(3);
  var yodaText = function(data) {
    var toSend = {text: data, completed: false};
    xhrRequest('PUT', url + '/' + id, JSON.stringify(toSend), function(response) {
      document.querySelector('#di'+id + ' div').textContent = toSend.text;
    })
  };
  yoda(document.querySelector('#di'+id + ' div').textContent, yodaText);
}

function yoda(str, cb) {
  var urlStr = 'https://yoda.p.mashape.com/yoda?sentence=' + encodeURIComponent(str);
  var xhr = new XMLHttpRequest();
  xhr.open('GET', urlStr);
  xhr.setRequestHeader("X-Mashape-Key", "KEjoG3sQWtmshlaiwkAEob887fgSp1pi544jsniIOqOgC9nIXm");
  xhr.send();
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      var data = xhr.responseText;
      cb(data);
    }
  };
}

getTodos();
addButton.addEventListener('click', addNewTodo);
