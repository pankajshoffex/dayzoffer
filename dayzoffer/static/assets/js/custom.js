$(document).ready(function() {
	//OWL CAROUSEL MULTIPLE SLIDER
  $("#owl-portfolio-item").owlCarousel({
    autoPlay: 3000,
    navigationText: ["", ""],
    navigation: true,
    pagination: false,
    itemsCustom: [
      [0, 1],
      [768, 5]
    ]
  });
});

onload = function(){
    for (var i = 0; i < document.images.length; i++) {
        centerImage(document.images[i]);
    }
};

function centerImage(img) {
    var container = img.parentNode;
    img.style.top = ((container.offsetHeight - img.offsetHeight) / 2) + "px";
    img.style.left = ((container.offsetWidth - img.offsetWidth) / 2) + "px";
}