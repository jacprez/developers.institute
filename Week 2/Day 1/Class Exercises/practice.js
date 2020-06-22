// Arrays - variables that hold multiple values

const numbers = new Array(1, 2, 3, 4)
console.log(numbers)


const fruits = ["apples", "oranges", "pears"];
console.log(fruits);

fruits[3] = 'grapes';
console.log(fruits);

fruits.push('mangos');
console.log(fruits);

fruits.pop();
console.log(fruits);

console.log(Array.isArray('hello'));
// true or false value





// Object literals - key value pairs 

const person = {
	firstName: 'John',
	lastName: 'Doe',
	age:30, 
	hobbies: ['music', 'movies', 'sports'],
	address: {
		street: '50 main st.',
		city: 'Boston',
		state: 'MA'
	}
}

console.log(person.hobbies[1]);
console.log(person.address.city);
console.log(person.age);
console.log(person);

// const { firstName, lastName } = person;
// console.log(firstName)

const { firstName, lastName, address: { city } } = person;
console.log(city);
person.email = 'john@gmail.com'
console.log(person)


const todos = [
	{
		id:1,
		text: 'Take out trash',
		isCompleted: true
	},
{
		id:2,
		text: 'Meeting',
		isCompleted: true
	},
	{
		id:3,
		text: 'Dentist',
		isCompleted: false
	}

];
console.log(todos);

console.log(todos[1].text);

const todoJSON = JSON.stringify(todos);
console.log(todoJSON);



// For loops

for(let i = 0; i < 10; i++) {
	console.log(i);
}

// While loops
let i = 0;
while(i < 10) {
	console.log(`While loop number is: ${i}`);
	i++;
}

const todos2 = [
	{
		id:1,
		text: 'Take out trash',
		isCompleted: true
	},
{
		id:2,
		text: 'Meeting',
		isCompleted: true
	},
	{
		id:3,
		text: 'Dentist',
		isCompleted: false
	}

];


for(let todo of todos2) {
	console.log(todo);
}






