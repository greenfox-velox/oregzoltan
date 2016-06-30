'use strict';

var pictureList = [
  'imgs/6095.jpg',
  'imgs/6096.jpg',
  'imgs/6098.jpg',
  'imgs/6099.jpg',
  'imgs/6100.jpg',
  'imgs/6101.jpg',
  'imgs/6109.jpg',
  'imgs/6111.jpg',
  'imgs/6112.jpg',
  'imgs/6115.jpg',
  'imgs/6116.jpg',
  'imgs/6117.jpg',
];

var counter = 0;
var actual = 0;
var actualSmall = 0;
var limit = 0;

var img_main = document.querySelector('.img_big');
img_main.setAttribute('src', pictureList[actual]);

var img_row = document.querySelectorAll('.img_small');
limit = actualSmall+4;
for (var i = actualSmall; i < limit; i++) {
  img_row[i].setAttribute('src', pictureList[i]);
}

var img_title = document.querySelector('h2');
img_title.textContent = img_main.getAttribute('src');

var buttonBL = document.querySelector('.big_left');
var buttonSL = document.querySelector('.small_left');
var buttonBR = document.querySelector('.big_right');
var buttonSR = document.querySelector('.small_right');

function bigToRight() {
  if (actual < pictureList.length-1) {
    actual++;
    img_main.setAttribute('src', pictureList[actual]);
    img_title.textContent = img_main.getAttribute('src');
  }
}

function bigToLeft() {
  if (actual > 0) {
    actual--;
    img_main.setAttribute('src', pictureList[actual]);
    img_title.textContent = img_main.getAttribute('src');
  }
}

function smallToRight() {
  if (actualSmall+4 < pictureList.length-1) {
    actualSmall++;
    limit = actualSmall+4;
    counter = 0;
    for (var i = actualSmall; i < limit; i++) {
      img_row[counter].setAttribute('src', pictureList[i]);
      counter++;
    }
  }
}

function smallToLeft() {
  if (actualSmall > 0) {
    actualSmall--;
    limit = actualSmall+4;
    counter = 0;
    for (var i = actualSmall; i < limit; i++) {
      img_row[counter].setAttribute('src', pictureList[i]);
      counter++;
    }
  }
}


buttonBL.addEventListener('click', bigToLeft);
buttonSL.addEventListener('click', smallToLeft);
buttonBR.addEventListener('click', bigToRight);
buttonSR.addEventListener('click', smallToRight);
