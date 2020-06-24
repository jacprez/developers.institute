// Exercise 1 



function checkDriverAge() {
	let age = prompt("What is your age?");
		if (Number(age) < 18) {
			console.log("Sorry, you are too young to drive this car. Powering off");
		} else if (Number(age) > 18) {
			console.log("Powering On. Enjoy the ride!");
		} else if (Number(age) === 18) {
			console.log("Congratulations on your first year of driving. Enjoy the ride!");
		}
}

checkDriverAge();


// Exercise 2

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(basket){
	let checkItem = prompt("Enter an item to see if it's in your cart: ")
	for (item in basket) {
		if (checkItem === item) {
			console.log(checkItem + " is in your basket.")
		} else {
			continue;
		}
	}
}


checkBasket(amazonBasket);

// Exercise 3

function changeEnough(array_of_coins, total_price){

	total_coins = (array_of_coins[0]*.25) + (array_of_coins[1]*.10) + (array_of_coins[2]*.05) + (array_of_coins[3]*.01)
	if (total_coins >= total_price) {
		return true
	} else {
		return false
	}
}


// Exercise 4

let shoppingList = ["banana", "orange" , "apple"];
// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let total = 0;
for (let item of shoppingList) {
	total += prices[item]
}
console.log(total)

// Exercise 5

function hotel_cost(){
	let number_of_nights = parseInt(prompt("Enter the number of nights you will be staying: "))
	return number_of_nights*140
}


function plane_ride_cost(){
	let destination = undefined;
	while (destination == undefined){
		destination = prompt("Where do you want to go?").toLowerCase()
		if (destination == "london") {
			console.log("The price of London is $183.")
			return 183
		} else if (destination == "paris") {
			console.log("The price of Paris is $220.")
			return 220
		} else {
			console.log("All other destinations are $300.")
			return 300
		}
	}
}




function rental_car_cost(){
	let days_to_rent_car = parseInt(prompt("How many days do you want to rent a car?"))
	if (days_to_rent_car > 10) {
		let discount = (days_to_rent_car*40)*.05
		let total = (days_to_rent_car*40) - discount;
		return total
	} else {
		return (days_to_rent_car*40)
	}
}

function total_vaca_cost() {
	let hotel = hotel_cost();
	let plane = plane_ride_cost();
	let car = rental_car_cost();

	return hotel + plane + car
}



console.log(total_vaca_cost());




