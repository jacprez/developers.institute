let str = 'This dinner is not that bad!'

let notIndex = str.indexOf("not");
let badIndex = str.indexOf("bad");

console.log(str);

if (badIndex > notIndex) {
	console.log(str.substring(0, notIndex) + "good");
}
else {
	console.log(str);
}
