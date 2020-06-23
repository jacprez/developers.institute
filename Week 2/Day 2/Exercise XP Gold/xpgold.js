// Exercise 1

let userPrompt = prompt("Type in a word: ")
let noVowels = userPrompt.replace(/[aeiouAEIOU]/g, '')
console.log(noVowels)

// Exercise 2

let userAnswer = prompt("Which language do you speak?")

switch(userAnswer) {
	case "French":
	case "french":
		console.log("Bonjour");
		break;
	case "English":
	case "english":
		console.log("Hello");
		break;
	case "Hebrew":
	case "hebrew":
		console.log("Shalom")
	default:
		console.log(":)")
}

// Exercise 3

let userGrade = Number(prompt("What is your grade?"))

if (userGrade >= 90) {
	console.log('A')
} else if (userGrade >= 80) {
	console.log('B')
} else if (userGrade >= 70) {
	console.log('C')
} else {
	console.log('D')
}

// Exercise 4
let userZip = prompt("Enter your zip code: ");
let checkZip = Number(userZip);

if (checkZip && userZip.length == 5) {
	console.log("Your zip is: " + checkZip)
} else {
	console.log("Error. " + userZip + " is not a valid response.")
}















