
var sliderArray = {"range1": "output1",
                    "range2": "output2"}
console.log(sliderArray);

// Update the current slider value (each time you drag the slider handle)


function updateSliderValues() {
  for (var sliderID in sliderArray) {

    var slider = document.getElementById(sliderID);
    var output = document.getElementById(sliderArray[sliderID]);
    output.innerHTML = slider.value;
  }
}

$(document).ready(function () {
  $(".dropdown-menu li a").click(function(){
    $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
    $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
  });
});

