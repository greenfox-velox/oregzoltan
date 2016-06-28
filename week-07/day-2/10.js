'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  grades : [],
  addgrade : function(grade) {
    this.grades.push(grade);
  },
  getAverage : function() {
    var total = 0;
    this.grades.forEach(function(e) {
      total += e;
    })
    return total/this.grades.length;
  }
};

student.addgrade(5);
student.addgrade(3);
student.addgrade(1);
console.log(student.getAverage());
