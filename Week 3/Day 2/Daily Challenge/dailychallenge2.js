let libButton = document.getElementById('lib-button');
let libIt = function() {
    let nounInput = document.getElementById("noun").value
    let adjInput = document.getElementById("adjective").value
    let nameInput = document.getElementById("person").value
    if (nounInput, adjInput, nameInput == ""){
        alert("Error, missing fields.")
    } else {
        let storyDiv = document.getElementById("story");
        storyDiv.innerHTML = `The ${adjInput} ${nounInput} is so ${adjInput}, I decided to call it ${nameInput}.`
    }
    
};
libButton.addEventListener('click', libIt);