



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
			console.log(computerNumber)
		}
	} else {
		alert("No problem, goodbye!");
	}
}

// Second Part


counter = 0;
function test(userNum, computerNum) {
	for (i = 0; i < 3; i++) {
		console.log(userNum);
		if (userNum == computerNum) {
			alert("Great, you won the game!")
			break;
		} else if (userNum > computerNum) {
			prompt(userNum + " is too big, guess again: ")
			counter += 1
			console.log(counter)
			// test()
		} else if (userNum < computerNum) {
			prompt(userNum + " is too small, guess again: ")
			counter += 1
			console.log(counter)
		} else {
			alert("Goodbye!")
		}
	}
}



// else if (counter > 3) {
// 		alert("You guessed 3 times. The computer's number is:", computerNum)
// 		console.log(counter)
// 	} 
