'use strict';

var myDog = (function () {
  var sound = 'woof';
  return {
    talk: function () {
      console.log(sound);
    }
  };
})();

myDog.talk();
