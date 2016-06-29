    // Add an item that says 'The Green Fox' to the asteroid list.
var asteroidList = document.querySelector('ul.asteroids');
var newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroid);

    // Add an item that says 'The Lamplighter' to the asteroid list.

newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Lamplighter';
asteroidList.appendChild(newAsteroid);

    // Add a heading saying 'I can add elements to the DOM!' to the .container.

var cont = document.querySelector('.container');
var heading = document.createElement('h1');
heading.textContent = 'I can add elements to the DOM!';
cont.appendChild(heading);

    // Add an image, any image, to the container.

var image = document.createElement('img');
image.setAttribute('src', 'https://avatars2.githubusercontent.com/u/17909652?v=3&s=460');
cont.appendChild(image);
