
var sliderArray = {"range1": "output1",
                    "range2": "output2",
                    "range3": "output3",
                    "range4": "output4",
                    "range5": "output5"}
console.log(sliderArray);

var genres = ["alt-rock", "alternative", "ambient",
"anime", "blues", "bossanova", "children", "chill",
"classical", "club", "country", "dance", "deep-house",
"disco", "disney", "dubstep", "edm", "electro", "electronic",
"folk", "funk", "groove", "guitar", "happy", "hardcore",
"heavy-metal", "hip-hop", "holidays", "house",
"indie", "indie-pop", "j-dance", "j-pop", "j-rock",
"jazz", "k-pop", "kids", "latin", "metal", "metalcore",
"new-release", "opera", "party", "piano",
"pop", "punk", "punk-rock", "r-n-b", "rainy-day",
"reggae", "road-trip", "rock", "rock-n-roll",
"romance", "sad", "salsa", "sleep", "soul", "spanish",
"study", "summer", "synth-pop", "tango", "techno",
"trance", "work-out"]

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