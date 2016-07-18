'use strict';

var Dog = function () {
  this.sound = 'woof';
};

Dog.prototype.talk = function () {
  return console.log(this.sound);
};

var vizsla = new Dog();
vizsla.talk();
