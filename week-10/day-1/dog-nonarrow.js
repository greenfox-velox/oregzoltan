'use strict';

var dog = function () {
  var sound = 'woof';
  return {
    talk: function () {
      console.log(sound);
    }
  };
}


var attila = dog();
attila.talk();
