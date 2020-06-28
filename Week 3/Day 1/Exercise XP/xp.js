// Exercise 1 
// 1. 
// document.body.children[0]
// let div = document.body.children[0]
// div.setAttribute("id", "socialNetworkNavigation")

// // 2.

// let li = document.createElement("li")

// let litext = document.createTextNode("Logout")

// li.appendChild(litext)

// document.body.appendChild(li)

// Exercise 2 
// 1. 
let pete = document.getElementsByClassName("list")[0].lastElementChild
pete.innerHTML = "Richard"
// 2. 
let ul = document.getElementsByClassName("list")
ul[0].firstElementChild.innerText = "Jackie"
ul[1].firstElementChild.innerText = "Jackie"
// 3.
let newli = document.createElement("li")

let newliText = document.createTextNode("Hey students");

newli.appendChild(newliText);

document.body.appendChild(newli)

document.body.children[1].appendChild(newli)

// 4.
let parent = document.getElementsByTagName("ul")[1]

let child = parent.children[1]

parent.removeChild(child)