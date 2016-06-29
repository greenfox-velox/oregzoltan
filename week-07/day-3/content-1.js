// 1. Alert the content of the header.

alert(document.querySelector('h1').innerHTML);

// 2. Write the content of the first paragraph to the console.

console.log(document.querySelector('p').innerHTML);

// 3. Alert the content of the second paragraph.

alert(document.querySelector('.other').innerHTML);

// 4. Replace the heading's content with 'New content'.

 document.querySelector('h1').innerHTML = 'New content';

// 5. Replace the last paragraph's content with the first paragraph's content.

document.querySelector('.result').innerHTML = document.querySelector('p').innerHTML;
