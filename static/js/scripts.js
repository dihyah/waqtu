//Get current date
var currentDate = document.getElementById("currentDate");
    let today = new Date().toLocaleDateString();
        currentDate.innerHTML = (today); 
    
//Get geolocation
var x = document.getElementById("location");
navigator.geolocation.getCurrentPosition(function(position){ 
    x.innerHTML = (position.coords.latitude+', '+position.coords.longitude);
});

//Disables submit button if user doesn't input anything.
document.querySelector('#input').onkeyup = function(){
    if (document.querySelector('#input').value === ''){
        document.querySelector('#submit').disabled = true;
    } else {
        document.querySelector('#submit').disabled = false;
        }
}

//setting up API base
//https://api.aladhan.com/v1/timingsByAddress/{today(dd-mm-yyy)}?address={location}&method=3
const api = {
  base: "https://api.aladhan.com/v1/timingsByAddress/"
}

//Event Listener Function on keypress on location searchbox
const input = document.getElementById("input");
input.addEventListener("keypress", event);

function event(evt){
    if (evt.keyCode == 13) {
    parse(input.value);
  }
}

//Parse URL for JSON data
function parse(location){
    fetch(`${api.base}{today}?address=${input.value}&method=3`)
    .then(location =>{
        return location.json();
    }).then(display);
}
        
//Extract JSON Data and Show various data
function display(location){
    let place = document.getElementById("place");
    place.innerText = `${location.data.meta.timezone}`;

    let fajr = document.getElementById('fajr');
    fajr.innerText = `${location.data.timings.Fajr}`

    let sunrise = document.getElementById('sunrise');
    sunrise.innerText = `${location.data.timings.Sunrise}`

    let dhuhr = document.getElementById('dhuhr');
    dhuhr.innerText = `${location.data.timings.Dhuhr}`

    let asr = document.getElementById('asr');
    asr.innerText = `${location.data.timings.Asr}`

    let maghrib = document.getElementById('maghrib');
    maghrib.innerText = `${location.data.timings.Maghrib}`

    let isha = document.getElementById('isha');
    isha.innerText = `${location.data.timings.Isha}`

}

//Set deadline
var countDownDate = new Date("Aug 7, 2021 00:00:00").getTime();

//Update countdown every 1 second
var y = setInterval(function(){

    //Get today's datetime
    var now = new Date().getTime();

    //Find the distance between now and countdown Date
    var distance = countDownDate - now;

    //Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    //Display the result in the element with id="timer"
    document.getElementById("timer").innerHTML = hours + "h " + minutes + "m " + seconds + "s ";

    //If countdown is finished, write some text
    if (distance < 0) {
        clearInterval(y);
        document.getElementById("timer").innerHTML = "TIME'S UP";
    }
}, 1000);


