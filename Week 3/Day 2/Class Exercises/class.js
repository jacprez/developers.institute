// Event Listeners

let x = document.getElementById("btn")
let y = document.getElementById("btn1")

y.addEventListener("click", RespondClick);
y.addEventListener("mouseover", RespondMouseOver);

x.addEventListener("click", RespondClick); 
x.addEventListener("mouseover", RespondMouseOver); 
x.addEventListener("mouseout", RespondMouseOut); 

function RespondClick() { 
            x.style.backgroundColor = "lightblue"
            y.style.backgroundColor = "lightblue"
		} 

function RespondMouseOver() { 
            console.log("My mouse is over the btn")
		} 

function RespondMouseOut() { 
            console.log("My mouse is out of the btn")
        }     







let button1 = document.getElementById("button1")
button1.onclick = function(){
	console.log("You clicked me!")
}



// Exercise 1

let button = document.getElementById("button")
let counter = 2
button.onclick = function insert_Row() {
	counter += 1
	let table = document.getElementById("sampleTable")
	let tableRow = document.createElement("tr")
	let td1 = document.createElement("td")
	let td2 = document.createElement("td")
	let td1text = document.createTextNode("Row"+ counter + " cell1")
	let td2text = document.createTextNode("Row"+ counter + " cell2")
	td1.appendChild(td1text)
	td2.appendChild(td2text)
	tableRow.appendChild(td1)
	tableRow.appendChild(td2)
	table.appendChild(tableRow)
}












