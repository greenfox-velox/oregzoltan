
    // Write the image's url to the console.

var fox = document.querySelector('img');
console.log(fox.getAttribute('src'));

    // Replace the image with a picture of yourself.

fox.setAttribute('src', 'https://avatars2.githubusercontent.com/u/17909652?v=3&s=460');

    // Make the link point to the Green Fox Academy website.

document.querySelector('a').setAttribute('href', 'http://www.greenfoxacademy.com/');

    // Disable the second button.

var second_button = document.querySelector('.this-one');
second_button.disabled = true;

    // Replace its text with 'Don't click me!'.

second_button.textContent = "Don't click me!";
