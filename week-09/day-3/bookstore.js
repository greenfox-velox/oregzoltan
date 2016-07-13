'use strict';

var mysql = require("mysql");

var con = mysql.createConnection({
  database: "bookstore",
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

con.query("SELECT book_name, aut_name FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id;",function(err,rows){
  if(err) {
    console.log(err.toString());
    return;
  }
  console.log("Data received from Db:\n");
  console.log(rows);
});

con.end();
