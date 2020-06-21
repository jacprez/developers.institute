const inputArr = [5,0,9,1,7,4,2,6,3,8];

// let bubbleSort = (inputArr) => {
//     let len = inputArr.length;
//     for (let i = 0; i < len; i++) {
//         for (let j = 0; j < len; j++) {
//             if (inputArr[j] > inputArr[j + 1]) {
//                 let tmp = inputArr[j];
//                 inputArr[j] = inputArr[j + 1];
//                 inputArr[j + 1] = tmp;
//             }
//         }
//     }
//     return inputArr;
// };

// console.log(inputArr)

let bubbleSort = (inputArr) => {
    let len = inputArr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 0; i < len; i++) {
            if (inputArr[i] > inputArr[i + 1]) {
                let tmp = inputArr[i];
                inputArr[i] = inputArr[i + 1];
                inputArr[i + 1] = tmp;
                swapped = true;
            }
        }
    } while (swapped);
    return inputArr;
};

console.log(bubbleSort(inputArr))

let reverseArray = inputArr.reverse();
console.log(reverseArray)
let stringArr = reverseArray.toString();
console.log(stringArr)
let joined = reverseArray.join(" ");
console.log(joined)
let joined2 = reverseArray.join(" + ");
console.log(joined2)