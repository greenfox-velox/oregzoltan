'use strict';
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('todo'));

var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;

var url = 'mongodb://localhost:27017/todo';

MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);

    var collection = db.collection('todos');
    collection.remove({});

    app.get('/todos', function(req, res) {
      collection.find().toArray(function (err, result) {
        if (err) {
          console.log(err);
        }
        res.send(result);
      });
    });

    var currentid = 0;
    app.post('/todos', function(req, res) {
      var newTodo = {
        'id': ++currentid,
        'text': req.body.text,
        'completed': false
      };
      collection.insert(newTodo, function(err, result){
          if (err) {
            console.log(err);
          }
        res.send(newTodo);
      });
    });

  app.put('/todos/:id', function(req, res) {
    collection.update({'id': parseInt(req.params.id)}, {$set:{'text': req.body.text, 'completed': true}}, function(err, result){
      if(err) {
        console.log(err.toString());
        return;
      }
    response(res, {id: +req.params.id, text: req.body.text, completed: req.body.completed});
    });
  });

  app.get('/todos/:id', function(req, res) {
    collection.find({'id': parseInt(req.params.id)}, function(err,row){
      if(err) {
        console.log(err.toString());
        return;
      }
      errorHandling(res, row[0]);
    });
  });

  app.delete('/todos/:id', function(req, res) {
    collection.remove({'id': parseInt(req.params.id)}, function(err,row){
      if(err) {
        console.log(err.toString());
        return;
      }
      response(res, {id: +req.params.id, text: req.body.text, completed: req.body.completed});
    });
  });
  }
});

function response(res, item) {
  if (item === undefined) {
    res.sendStatus(404);
  } else {
    res.send(item);
  }
}

app.listen(3000);
