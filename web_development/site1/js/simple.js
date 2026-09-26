var ul = document.getElementById("languages");

ul.onclick = function(event) {
    var languages = event.target.innerHTML;
    var selection = document.getElementById("selection");
    selection.innerHTML = "You chose " + languages;
    // alert(li.innerHTML)
}

