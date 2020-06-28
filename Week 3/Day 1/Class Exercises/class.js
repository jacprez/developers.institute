  // <div>Users:</div>
  // <ul>
  //   <li>John</li>
  //   <li>Pete</li>
  // </ul>


// document.body.children[0]
// document.body.firstElementChild

// document.body.children[1]
// document.body.firstElementChild.nextElementSibling

// let ul = document.body.children[1]
// ul.children[1]
// ul.lastElementChild


// Access the div
document.body.getElementsByTagName("div")
document.body.getElementsByTagName("div")[0]


// Adding an element dynamically
let paragraph = document.createElement("p")
let text = document.createTextNode("I love coding")
paragraph.appendChild(text)
let div = document.getElementsByTagName("div")[0]
div.appendChild(paragraph)
