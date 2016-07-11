'use strict';

var http = require('http');

var server = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  var currentTime = new Date();
  var time =  currentTime.getHours() + ":" + currentTime.getMinutes();
  res.end(req.url + ' ' + req.method + ' ' + time);
});

server.listen(3000, '127.0.0.1');
