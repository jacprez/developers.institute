// Exercise 1
let userAge = Number(prompt("How old are you? Enter your age: "))

if (userAge < 18) {
	alert("Sorry, you are too young to drive this car. Powering off")
} else if (userAge == 18) {
	alert("Congratulations on your first year of driving. Enjoy the ride!")
} else {
	alert("Powering On. Enjoy the ride!")
}


// Exercise 2

let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}
// Prediction: will display 'Exactly!'


// Exercise 3

let b = 2 + 2;

switch (b) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}
// Prediction: will display 'Right!'


// Practice
let users = [
    {
        username: "Sarah",
        password: 123,
        friends: ["max", "tom"],
        pets : {
            numberPets : 2,
            typePets : ["dog", "cat"],
            favoriteFood : {
                dog : "candy",
                cat : "milk"
            }
        }
    }
]


// 1. get the numberPets

//     console.log(users[0].pets.numberPets);

// 2. get the 2nd type of pet
//     console.log(users[0].pets.typePets[1]);
// 3; What is the favorite food of the cat
//     console.log(users[0].pets.favoriteFood["cat"]); //
//     console.log(users[0].pets.favoriteFood.cat);



