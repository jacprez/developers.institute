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
while (userInput < 10) {
	userInput = prompt("Try again. Enter a number larger than 10: ")
}

// Exercise 4

let people = ["Greg", "Mary", "Devon", "James"];

for (let i in people) {
	console.log(people[i])
}

people.shift();
console.log(people);
people[2] = "Jason"
console.log(people);
people.push("Jackie")
console.log(people)


for (let name of people) {
	console.log(name)
	if (name === "Mary"){
		break;
	}
}
console.log(people.indexOf("Mary"));
console.log(people.indexOf("Foo"));

let last = people[people.length - 1]
console.log(last)

// Exercise 5

const age = [20,5,12,43,98,55];
// Sum
let sum = 0
for (let num of age) {
	sum += num
}
console.log(sum)
// Even 
for (numbers of age) {
	if (numbers%2 == 0) {
		console.log(numbers, "is even")
	} else {
		console.log(numbers, "is odd")
	}
}
// Largest number

let maxNum = Math.max.apply(0,age);
console.log(maxNum)












