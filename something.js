updateValues()

var sliderArray = {"range1": "output1",
                    "range2": "output2"}
console.log(sliderArray);

// Update the current slider value (each time you drag the slider handle)


function updateValues() {
  for (var sliderID in sliderArray) {

    var slider = document.getElementById(sliderID);
    var output = document.getElementById(sliderArray[sliderID]);
    output.innerHTML = slider.value;
  }
}