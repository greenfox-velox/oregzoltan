'use strict';

var express = require('express');
var app = express();

app.get('*', function(req, res) {
  var currentTime = new Date();
  var time =  currentTime.getHours() + ":" + currentTime.getMinutes();
  res.send(req.path + ' ' + req.method + ' ' + time);
});

app.listen(3000);
