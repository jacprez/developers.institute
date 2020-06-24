
// function get_age(){
// 	return Number(prompt("Enter your age: "));
// }

// get_age();


// function doubleNum(num){
// 	return num*2;
// }


// let user_age = get_age();
// console.log("Double your age is " + doubleNum(user_age));




function changeEnough(array_of_coins, total_price){
	
	let quarters = array_of_coins[0]*.25
	let dimes = array_of_coins[1]*.10
	let nickels = array_of_coins[2]*.05
	let pennies = array_of_coins[3]*.01
	totalCoins = quarters + dimes + nickels + pennies
	if (totalCoins >= total_price) {
		return true
	} else {
		return false
	}
}



