// Exercise 1

let me = ["my","favorite","color","is","blue"]
console.log(me.toString())
console.log(me.join())
console.log(me.join("+"))

// Exercise 2

let str1 = 'mix'
let str2 = 'pod'
let newWord = str2.slice(0,2) + str1.slice(2) + " " + str1.slice(0,2) + str2.slice(2)
console.log(newWord.toString())


// Exercise 3

let firstNum = Number(prompt("Enter a number: "));
let secondNum = Number(prompt("Enter another number: "));
let sum = firstNum + secondNum
alert(firstNum + " + " + secondNum + " = " + sum);