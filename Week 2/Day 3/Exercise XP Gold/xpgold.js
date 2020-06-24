
// Exercise 1
const GUEST_LIST = {
	Randy: "Germany",
	Karla: "France",
	Wendy: "Japan",
	Norman: "England",
	Sam: "Argentina"
}

let userInput = prompt("What is your name?");

for (let name in GUEST_LIST) {
	if (userInput === name) {
		console.log(`Hi! I'm ${name}, and I'm from ${GUEST_LIST[name]}`)
	} else if (userInput != name) {
		console.log("Hi I'm a guest.")
	} else {
		break;
	}
}