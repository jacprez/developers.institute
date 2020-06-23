// Exercise 1 


let favColors = ['blue', 'black', 'white', 'teal']

for (i = 0; i < favColors.length; i++){
	console.log("My #1 choice is", favColors[i])
}

// Exercise 2

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let secretSoc = ''

for (i = 0; i < names.length; i++) {
	names.sort();
	let firstLet = names[i].charAt(0)
	secretSoc += firstLet

	
}
console.log("The name of your secret society is",secretSoc)

// Exercise 3 


let userInput = Number(prompt("Enter a number larger than 10: "))
if (userInput < 10) {
	prompt(Enter)
}