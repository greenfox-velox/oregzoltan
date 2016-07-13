'use strict';
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('todo'));
var mysql = require("mysql");

var con = mysql.createConnection({
  database: "todos",
  host: "localhost",
  user: "root",
  password: "velox"
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.get('/todos', function(req, res) {
    con.query('SELECT * FROM todo;',function(err,rows){
      if(err) {
        console.log(err.toString());
        return;
      }
      res.send(rows);
    });
});

app.get('/todos/:id', function(req, res) {
  con.query('SELECT * FROM todo WHERE id =' +req.params.id, function(err,row){
    if(err) {
      console.log(err.toString());
      return;
    }
    errorHandling(res, row[0]);
  });
});

function createNewTodo(id, text) {
  var newTodo = {
    'completed': false,
    'id': id,
    'text': text
  }
  return newTodo;
}

app.post('/todos', function(req, res) {
  con.query('INSERT INTO todo VALUES (0, "' + req.body.text + '", 0)', function(err,row){
    if(err) {
      console.log(row);
      return;
    }
  res.send(createNewTodo(row.insertId, req.body.text));
  });
});

app.put('/todos/:id', function(req, res) {
  con.query('UPDATE todo SET text = "' + req.body.text + '", completed = 1 WHERE id = ' + req.params.id, function(err,row){
    if(err) {
      console.log(err.toString());
      return;
    }
  errorHandling(res, {id: +req.params.id, text: req.body.text, completed: true});
  });
});

app.delete('/todos/:id', function(req, res) {
  con.query('DELETE FROM todo WHERE id = ' + req.params.id, function(err,row){
    if(err) {
      console.log(err.toString());
      return;
    }
  errorHandling(res, {id: +req.params.id, text: req.body.text, completed: true});
  });
});

function errorHandling(res, item) {
  if (item === undefined) {
    res.sendStatus(404);
  } else {
    res.send(item);
  }
}

app.listen(3000);
