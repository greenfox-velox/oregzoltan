'use strict';
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

var data = [
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
  res.send(data);
});

app.get('/todos/:id', function(req, res) {
  res.send(data.filter(function (e) {
    if (e.id === +req.params.id) {
      return e;
    }
  })[0]);
});

var currentId = data.length;
function createNewTodo(text) {
  var newTodo = {
    'completed': false,
    'id': ++currentId,
    'text': text
  }
  data.push(newTodo);
  return newTodo;
}

app.post('/todos', function(req, res) {
  res.send(createNewTodo(req.body.text));
});

app.put('/todos/:id', function(req, res) {
  res.send(data.filter(function (e) {
    if (e.id === +req.params.id) {
      e.completed = true;
      e.text = req.body.text;
      return e;
    }
  })[0]);
});

app.delete('/todos/:id', function(req, res, next) {
  res.send(data.filter(function (e) {
    if (e.id === +req.params.id) {
      e.destroyed = true;
      data.splice(data.indexOf(e), 1);
      return e;
    }
  })[0]);
  res.sendStatus(404);
});

// app.use(function(err, req, res, next) {
// })
app.listen(3000);
