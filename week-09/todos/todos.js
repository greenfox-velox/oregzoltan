'use strict';
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

var todoList = [
  {
    'completed': false,
    'id': 1,
    'text': 'Buy milk'
  },
  {
    'completed': false,
    'id': 2,
    'text': 'Make dinner'
  },
  {
    'completed': false,
    'id': 3,
    'text': 'Save the world'
  }
];

app.get('/todos', function(req, res) {
  res.send(todoList);
});

app.get('/todos/:id', function(req, res) {
  res.send(todoList.filter(function (e) {
    if (e.id === +req.params.id) {
      return e;
    }
  })[0]);
});

var currentId = todoList.length;
function createNewTodo(text) {
  var newTodo = {
    'completed': false,
    'id': ++currentId,
    'text': text
  }
  todoList.push(newTodo);
  return newTodo;
}

app.post('/todos', function(req, res) {
  res.send(createNewTodo(req.body.text));
});

app.put('/todos/:id', function(req, res) {
  res.send(todoList.filter(function (e) {
    if (e.id === +req.params.id) {
      e.completed = true;
      e.text = req.body.text;
      return e;
    }
  })[0]);
});

app.delete('/todos/:id', function(req, res) {
  res.send(todoList.filter(function (e) {
    if (e.id === +req.params.id) {
      e.destroyed = true;
      todoList.splice(todoList.indexOf(e), 1);
      return e;
    }
  })[0]);
});

// app.get('*', function(req, res) {
//     res.sendfile('./index.html');
// });

// app.use(function(err, req, res, next) {
// res.sendStatus(404);
// });
app.listen(3000);
