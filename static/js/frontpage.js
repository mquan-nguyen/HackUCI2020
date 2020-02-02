something = document.getElementById("hidden");
console.log("here:", something)

var sliderArray = {"range1": "output1",
"range2": "output2",
"range3": "output3",
"range4": "output4",
"range5": "output5"}

var genres = ["Alt-rock", "Alternative", "Ambient",
"Anime", "Blues", "Bossanova", "Children", "Chill",
"Classical", "Club", "Country", "Dance", "Deep-house",
"Disco", "Disney", "Dubstep", "EDM", "Electro", "Electronic",
"Folk", "Funk", "Groove", "Guitar", "Happy", "Hardcore",
"Heavy-metal", "Hip-hop", "Holidays", "House",
"Indie", "Jndie-pop", "J-dance", "J-pop", "J-rock",
"Jazz", "K-pop", "Kids", "Latin", "Metal", "Metalcore",
"New-release", "Opera", "Party", "Piano",
"Pop", "Punk", "Punk-rock", "R-n-B", "Rainy-day",
"Reggae", "Road-trip", "Rock", "Rock-n-roll",
"Romance", "Sad", "Salsa", "Sleep", "Soul", "Spanish",
"Study", "Summer", "Synth-pop", "Tango", "Techno",
"Trance", "Work-out"]

// Update the current slider value (each time you drag the slider handle)


function updateSliderValues() {
for (var sliderID in sliderArray) {

var slider = document.getElementById(sliderID);
var output = document.getElementById(sliderArray[sliderID]);
output.innerHTML = slider.value;
}
}

function updateDropdown(html_object) {
topDropdown = document.getElementById("select-button");
topDropdown.innerHTML = html_object.innerHTML;

something = document.getElementById("hidden");
console.log(something)
something.value = html_object.innerHTML.toLowerCase();
}

genres.forEach(populateDropdown);
function populateDropdown(item) {
dropdown_text = document.getElementById("dropdown-text");
option = document.createElement("BUTTON");
option.classList.add("dropdown-item");
option.type = "button";
option.onclick = function() { updateDropdown(this)};
option.innerHTML = item;

dropdown_text.appendChild(option)



}

function validateForm() {
    console.log("VALIDATING...")
  var x = document.forms[0]["genre"].value;
  if (x == "") {
    alert("You must pick a genre!");
    return false;
  }
}

$(document).ready(function() {
    //option A
    $("form").submit(function(e){
        if (validateForm() == false) {
            e.preventDefault(e);
        }
    });
});