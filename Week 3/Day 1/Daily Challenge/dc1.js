// Create an array called allBooks. This array contain objects. Each object is a book that has 4 keys : title, author,image(a url) and alreadyRead which is a boolean.
// Initiate the array with 2 books of your choice.
// Requirements:
// On the page you have to render the books inside a table.
// For each book :
// You have to display the book’s title then “written by” and then the book’s author (Ex: HarryPotter written by JKRolling)
// The width of the image has to be set to 100.
// If the book is already read. Set the color of the book details to red

let allBooks = [
	{
		"title":"Harry Potter",
		"author":"JK Rolling",
		"image": "https://api.time.com/wp-content/uploads/2014/07/301386_full1.jpg?w=600&quality=85",
		"alreadyRead": false
	},
	{
		"title":"To Kill A Mockingbird",
		"author":"Harper Lee",
		"image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg/440px-To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
		"alreadyRead": true
	}
]


let table = document.createElement("table");
let row = document.createElement("tr");
table.appendChild(row);

let thName = document.createElement("th");
thName.innerHTML = "Title"
let thAuthor = document.createElement("th")
thAuthor.innerHTML = "Author"
let thimage = document.createElement("th")
thimage.innerHTML = "Image"


row.appendChild(thName);
row.appendChild(thAuthor);
row.appendChild(thimage);

for (book of allBooks) {
	let bookrow = document.createElement("tr");	
	table.appendChild(bookrow);
	let cellName = document.createElement("td");
	cellName.innerHTML = book["title"];
	if (book["alreadyRead"] == true) {
		bookrow.style.color = "red"
	}
	bookrow.appendChild(cellName);
	let cellAuthor = document.createElement("td");
	cellAuthor.innerHTML = book["author"];
	bookrow.appendChild(cellAuthor);
	let cellImage = document.createElement("td");
	let img = document.createElement("img");
	img.setAttribute("src", book["image"]);
	img.style.height = "100px"
	cellImage.appendChild(img);
	bookrow.appendChild(cellName);
	bookrow.appendChild(cellAuthor);
	bookrow.appendChild(cellImage);
}
document.body.appendChild(table);



// let trHarry = document.createElement("tr")
// let trTKAM = document.createElement("tr")

// let keysFirstObj = Object.keys(allBooks[0])
// let keysSecondObj = Object.keys(allBooks[1])

// for(i = 0; i < keysFirstObj.length; i++){
// 	let headers = document.createTextNode(keysFirstObj[i])

// }


// function addParagraph(sentence){
// 	let p = document.createElement("p")
// 	let text = document.createTextNode(sentence)
// 	p.appendChild(text)

// }