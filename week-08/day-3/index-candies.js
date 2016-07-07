'use strict';

var creCan = document.querySelector('.creCan');
var buyLol = document.querySelector('.buyLol');
var numCan = document.querySelector('.numCan');
var numLol = document.querySelector('.numLol');
var candies = 0;
var lollipops = 0;
setCandies();
setLollipops();

function setCandies() {
  numCan.textContent = 'Number of candies: ' + candies;
}

function setLollipops() {
  numLol.textContent = 'Number of lollipops: ' + lollipops;
}

function createCandies() {
  candies++;
  setCandies();
}

function buyLollipop() {
  if (candies >= 100) {
    candies -= 100;
    lollipops++;
    setCandies();
    setLollipops();
  }
}

setInterval(function () {
  if (lollipops >= 100){
    candies += Math.floor(lollipops / 10);
    setCandies();
  }
  if (candies === 10000) {
    alert('WIN!');
  }
}, 1000);

creCan.addEventListener('click', createCandies);
buyLol.addEventListener('click', buyLollipop);
