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
];
var actual = 0;
var img_main = document.querySelector('.img_big');
img_main.setAttribute('src', pictureList[actual]);

var img_row = document.querySelectorAll('.img_small');
for (var i = 0; i < 4; i++) {
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


function smallToLeft() {

}
function smallToRight() {

}
buttonBL.addEventListener('click', bigToLeft);
buttonSL.addEventListener('click', smallToLeft);
buttonBR.addEventListener('click', bigToRight);
buttonSR.addEventListener('click', smallToRight);
