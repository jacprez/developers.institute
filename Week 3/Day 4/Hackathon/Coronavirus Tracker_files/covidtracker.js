



// $(document).ready(function(){
// 	init()


// 	function init(){
// 		let url = "https://api.covid19api.com/summary"
// 		$.get(url, function(data){
// 			console.log(data)
// 		})
// 	}

// })


// window.onload = function(){
// 	let stats = getCovidStats();
// }

// function getCovidStats(){
// 	fetch("https://api.covid19api.com/summary")
// 	.then(function(resp) { return resp.json() })
// 	.then(function(data){
// 		console.log(data)
// 		let gblNewConfirmed = data.Global.NewConfirmed
// 		let gblNewDeaths = data.Global.NewDeaths
// 		let gblNewRecovered = data.Global.NewRecovered
// 		let gblTotalConfirmed = data.Global.TotalConfirmed
// 		let gblTotalDeaths = data.Global.TotalDeaths
// 		let gblTotalRecovered = data.Global.TotalRecovered
// 		let lastUpdated = data.Date

// 		document.getElementById("lastUpdate").innerHTML = "Last updated: " + lastUpdated.substring(0,10)
// 		document.getElementById("gbNewConfirm").innerHTML = gblNewConfirmed.toLocaleString('en')
// 		document.getElementById("gbNewDeaths").innerHTML = gblNewDeaths.toLocaleString('en')
// 		document.getElementById("gbNewRecovered").innerHTML = gblNewRecovered.toLocaleString('en')
// 		document.getElementById("gbTotalConfirmed").innerHTML = gblTotalConfirmed.toLocaleString('en')
// 		document.getElementById("gbTotalDeaths").innerHTML = gblTotalDeaths.toLocaleString('en')
// 		document.getElementById("gbTotalRecovered").innerHTML = gblTotalRecovered.toLocaleString('en')
		
// 		let countries = data.Countries
// 		console.log(countries)
// 		let countryList = []
// 		for (let i in countries){
// 				countryList += countries[i].Country + ", "
				
// 		}console.log(countryList)
		



// 	})
// 	.catch(function(){
// 		console.log("error")
// 	})
	
// 	setTimeout(getCovidStats, 43200000)
// }

// let searchButton = document.getElementById("searchBtn")
// searchButton.onclick = function searchWord(event) {
// 			event.preventDefault();
// 			let searchTerm = document.getElementById("searchInput").value;
// }



let data;

function getCovidStats(){
	fetch("https://api.covid19api.com/summary")
	.then(function(resp) { return resp.json() })
	.then(function(data) { useData(data)})
}
window.onload = function(){
	getCovidStats();
}

function useData(result){
	displayGlobalStats(result);
	countryData(result);
}

function displayGlobalStats(result){
	// data = result;
	console.log(result)
		let gblNewConfirmed = result.Global.NewConfirmed
		let gblNewDeaths = result.Global.NewDeaths
		let gblNewRecovered = result.Global.NewRecovered
		let gblTotalConfirmed = result.Global.TotalConfirmed
		let gblTotalDeaths = result.Global.TotalDeaths
		let gblTotalRecovered = result.Global.TotalRecovered
		let lastUpdated = result.Date

		document.getElementById("lastUpdate").innerHTML = "Last updated: " + lastUpdated.substring(0,10)
		document.getElementById("gbNewConfirm").innerHTML = gblNewConfirmed.toLocaleString('en')
		document.getElementById("gbNewDeaths").innerHTML = gblNewDeaths.toLocaleString('en')
		document.getElementById("gbNewRecovered").innerHTML = gblNewRecovered.toLocaleString('en')
		document.getElementById("gbTotalConfirmed").innerHTML = gblTotalConfirmed.toLocaleString('en')
		document.getElementById("gbTotalDeaths").innerHTML = gblTotalDeaths.toLocaleString('en')
		document.getElementById("gbTotalRecovered").innerHTML = gblTotalRecovered.toLocaleString('en')


}

// function countryList(result){
// 	data=result;
// 	let countryArr = data.Countries;
// 	document.getElementById('searchBtn').addEventListener('click', () => {
// 				let searchTerm=document.getElementById('searchInput').value;
// 				for (let i in countryArr){
// 					if (searchTerm == countryArr[i].Country){
// 						console.log(countryArr[i]);
// 					}



// let countryArr = data.Countries
// console.log(countryArr)

	
// function searchCountry() {
// 	let data;
// 	console.log(data)
// 	let input = document.getElementById("searchInput");
// 	let filter = input.value.toUpperCase();
// 	let table = document.createElement("table");

// 	tr = table.getElementsByTagName("tr");
// 	for (i = 0; i < tr.length; i++) {
// 		td = tr[i].getElementsByTagName("td")[0];
// 		if (td) {
// 		txtValue = td.textContent || td.innerText;
// 		if (txtValue.toUpperCase().indexOf(filter) > -1) {
// 			tr[i].style.display = "";
// 		} else {
// 			tr[i].style.display = "none";
// 		}
// 		}       
// 	}
// }




function countryData(result){
	data=result;
	let countryArr = data.Countries;
	document.getElementById('searchBtn').addEventListener('click', () => {
		let searchTerm=document.getElementById('searchInput').value;
		for (let i in countryArr){
			if (searchTerm == countryArr[i].Country){
				document.getElementById("countryStats").style.display = "grid";
				let countryName = countryArr[i].Country;
				document.getElementById("countryHeader").innerHTML = countryName;
				let countryNewConfirm = countryArr[i].NewConfirmed;
				let countryNewDeaths = countryArr[i].NewDeaths;
				let countryNewRecovered = countryArr[i].NewRecovered;
				let countryTotalConfirmed = countryArr[i].TotalConfirmed;
				let countryTotalDeaths = countryArr[i].TotalDeaths;
				let countryTotalRecovered = countryArr[i].TotalRecovered;
				document.getElementById("countryNewConfirm").innerText = countryNewConfirm.toLocaleString('en');
				document.getElementById("countryNewDeaths").innerText = countryNewDeaths.toLocaleString('en');
				document.getElementById("countryNewRecovered").innerText = countryNewRecovered.toLocaleString('en');
				document.getElementById("countryTotalConfirmed").innerText = countryTotalConfirmed.toLocaleString('en');
				document.getElementById("countryTotalDeaths").innerText = countryTotalDeaths.toLocaleString('en');
				document.getElementById("countryTotalRecovered").innerText = countryTotalRecovered.toLocaleString('en');
				document.getElementById("jumbotronDiv").style.padding = "0px";
				document.getElementById("jumbotronDiv").style.padding = "0px";
				document.getElementsByClassName("display-4")[0].style.fontSize = "20px"
				break;
			}else{
				console.log(searchTerm + " not found.");
			}

		}
	})
}
// Afghanistan



// function formatCountryStats(countryIndex)

// 	console.log(countryArray)
// 	for (let i in countryArray) {
// 		console.log(countryArray[i])
// 	}
			
// let searchButton = document.getElementById("searchBtn");
// let form = document.forms.searchButton;


// form.addEventListener("submit", test)
// function test(e){
// 	let input = document.getElementById("searchInput").value;
// 	e.preventDefault();
// }



// let searchInput = document.getElementById("searchInput")
// searchInput.addEventListener('keyup', function(e){
// 			let term = e.target.value.toLowerCase()
// 				console.log(term)
// 			if (term){
// 				searchCountry(term)
// 			}

// 			})
			

		



// 	})
// 	.catch(function(){
// 		console.log("error")
// 	})
	
// 	setTimeout(getCovidStats, 43200000)


// let searchButton = document.getElementById("searchBtn")
// searchButton.onclick = function searchWord(event) {
// 			event.preventDefault();
// 			let searchTerm = document.getElementById("searchInput").value;
// }

