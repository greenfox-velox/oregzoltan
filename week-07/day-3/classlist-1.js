    // Does cat have a cat class?
    // If so, alert 'YEAH CAT!'

var elements = document.querySelectorAll('p');
elements.forEach(function (e) {
  if (e.textContent === 'cat' && e.classList.contains('cat')) {
    alert ('YEAH CAT!');
  }
})

    // If dolphin has a 'dolphin' class, replace apple's content with 'pear'

elements.forEach(function (e) {
  if (e.textContent === 'dolphin' && e.classList.contains('dolphin')) {
    document.querySelector('.apple').textContent = document.querySelector('.pear').textContent;
  }
})

    // If apple has an 'apple' class, replace cat's content with 'dog'

elements.forEach(function (e) {
  if (e.textContent === 'apple' && e.classList.contains('apple')) {
    document.querySelector('.cat').textContent = 'dog';
  }
})

    // Make apple red

document.querySelector('.apple').classList.add('red');

    // Make balloon less balloon-like

document.querySelector('.balloon').classList.remove('balloon')
