'use strict';

var myDog = (function () {
  var sound = 'woof';
  function publicTalk () {
    console.log(sound);
  }
  return {
    talk: publicTalk
  };
})();

myDog.talk();
