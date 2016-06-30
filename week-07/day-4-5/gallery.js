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
var img_main = document.querySelector('.img_big');
img_main.setAttribute('src', pictureList[0]);

var img_row = document.querySelectorAll('.img_small');
for (var i = 0; i < 4; i++) {
  img_row[i].setAttribute('src', pictureList[i]);

}
// var pictureList = document.querySelectorAll('.pictureList');
// for (var i = 0; i < pictureList.length; i++) {
//   pictureList[i].src = pictureListUrls[i];
// }
