let sentence = prompt("Enter some words (commas seperated)");
let words = sentence.split(",")
console.log(words)

// for (item of words) {
// 	let trimmed_word = item.trim();
// 	console.log(trimmed_word)
// }

for (i in words) {
	words[i] = words[i].trim();
}

console.log(words)


let longest = 0;
for (word of words){
	if (word.length > longest) {
		longest = word.length
	}
}

console.log(longest)


let star_line = "*".repeat(longest + 4)

console.log(star_line);
for (word of words) {
	let line = ("* " + word + " ".repeat(longest-word.length + 1) + "*")
	console.log(line)
}
console.log(star_line);

