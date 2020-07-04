// Exercise 1

// let ptags = document.getElementsByTagName('p');
// ptags.className = "para_article"

// // ptags[3].remove()

// let headingTwo = document.getElementById("heading2");
// headingTwo.addEventListener("click", removeElement);


// function removeElement() {
// 	let head2 = document.getElementById("heading2");
// 	head2.remove()
// };


// // let h1 = document.getElementsByTagName("h1")[0]
// // let sizeOfFont = (Math.floor(Math.random() * 100) + 1) + "px"
// // console.log(sizeOfFont)
// // h1.style.fontSize = sizeOfFont

// document.getElementsByTagName("h1")[0].setAttribute("id", "heading1");
// let head1 = document.getElementById("heading1")
// head1.addEventListener("click", removeHead1);

// function removeHead1() {
// 	let head1 = document.getElementById("heading1");
// 	head1.remove()
// };

// getBold_items()


let strong = document.getElementsByTagName("strong")
let allBold = []

for (elem of strong){
	allBold += elem.innerHTML + " "
}

console.log(allBold)

highlight()






