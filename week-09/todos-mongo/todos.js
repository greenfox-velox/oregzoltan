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

    // do some work here with the database.
    var collection = db.collection('todos');
    collection.remove({});
    // //Create some users
    // var todo1 = {id: 1, text: 'eat', completed: false};
    // var todo2 = {id: 2, text: 'drink', completed: false};
    // var todo3 = {id: 3, text: 'sleep', completed: false};
    //
    // // Insert some users
    // collection.insert([todo1, todo2, todo3], function (err, result) {
    //   if (err) {
    //     console.log(err);
    //   } else {
    //     console.log('Inserted %d documents into the "users" collection. The documents inserted with "_id" are:', result.length, result);
    //   }
    // });
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
    collection.update({'id': req.params.id}, {$set:{'completed': true}}, function(err, result){
      if(err) {
        console.log(err.toString());
        return;
      }
    errorHandling(res, {id: +req.params.id, text: req.body.text, completed: req.body.completed});
    });
  });
}});

  app.delete('/todos/:id', function(req, res) {
    collection.remove({}, function(err,row){
      if(err) {
        console.log(err.toString());
        return;
      }
      errorHandling(res, {id: +req.params.id, text: req.body.text, completed: req.body.completed});
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

//
// app.get('/todos/:id', function(req, res) {
//   con.query('SELECT * FROM todo WHERE id =' +req.params.id, function(err,row){
//     if(err) {
//       console.log(err.toString());
//       return;
//     }
//     errorHandling(res, row[0]);
//   });
// });
//
//
// app.put('/todos/:id', function(req, res) {
//   con.query('UPDATE todo SET text = "' + req.body.text + '", completed = ' + req.body.completed + ' WHERE id = ' + req.params.id, function(err,row){
//     if(err) {
//       console.log(err.toString());
//       return;
//     }
//   errorHandling(res, {id: +req.params.id, text: req.body.text, completed: req.body.completed});
//   });
// });
//
// app.delete('/todos/:id', function(req, res) {
//   con.query('DELETE FROM todo WHERE id = ' + req.params.id, function(err,row){
//     if(err) {
//       console.log(err.toString());
//       return;
//     }
//     errorHandling(res, {id: +req.params.id, text: req.body.text, completed: req.body.completed});
//   });
// });
//
