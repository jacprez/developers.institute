let startingNum = ""
let numList = []
let operator = ""



function num (int) {
	startingNum += int
	console.log(startingNum);
	return startingNum;
}


function math (oper) {
	numList.push(startingNum)
	startingNum=""
	operator = oper;
	console.log(operator);
	console.log(numList);
}

function equal () {
	numList.push(startingNum)
	let a = Number(numList[0])
	let b = Number(numList[1])

	switch(operator){
		case "+": 
			console.log(a+b)
			return a+b;
			break;
		case "-":
			console.log(a-b)
			return a-b;
			break;
		case "/":
			console.log(a/b)
			return a/b;
			break;
		case "*":
			console.log(a*b)
			return a*b;
			break;

	}
}






