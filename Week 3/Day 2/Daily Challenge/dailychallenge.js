let button = document.getElementById("mybtn")
button.addEventListener("mouseover", mOver)
button.addEventListener("mouseout", mOut)
button.addEventListener("click", function() {
    alert("You clicked me!")
})

function mOver() {
    button.style.backgroundColor = "black"
    button.innerText = "Mouse over"
    button.style.color = "white"
}

function mOut() {
    button.style.backgroundColor = 'white'
    button.innerText = "Mouse out"
    button.style.color = "black"

}