



// First Part

function playTheGame() {
	let wantsToPlay = confirm("Do you want to play the game?")
	if (wantsToPlay === true){
		let userNumber = Number(prompt("Enter a number between 1 and 10: "));
		if (isNaN(userNumber)) {
			alert("Sorry " + userNumber + " is not a number, goodbye!");
		} else if (userNumber > 10 || userNumber < 0) {
			alert("Sorry " + userNumber + " not a good number, goodbye!");
		} else {
			let computerNumber = Math.floor(Math.random() * 11)
			test(userNumber, computerNumber)
		}
	} else {
		alert("No problem, goodbye!");
	}
}

// Second Part

counter = 0;

function test(userNum, computerNum) {
	if (userNum == computerNum) {
		alert("Great, you won the game!")
	} else if (userNum > computerNum) {
		let guess = prompt(userNum + " is too big, guess again: ")
		counter += 1
		test(guess, computerNum)
	} else if (userNum < computerNum) {
		let guess = prompt(userNum + " is too small, guess again: ")
		counter += 1
		test(guess, computerNumber)
	} else if (counter > 3) {
		alert("You guessed 3 times. The computer's number is:", computerNum)
	} else {
		alert("Goodbye!")
	}
}





