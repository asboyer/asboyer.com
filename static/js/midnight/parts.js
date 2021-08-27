function shuffle(array) {
  var currentIndex = array.length,  randomIndex;

  // While there remain elements to shuffle...
  while (currentIndex != 0) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }

  return array;
}

$(document).ready(function(){
    $.getJSON("/data/midnight/specs.json", function(json) {
        // generate random number between 0 and 4
        var number = 0
        document.getElementById('midnight-specs').style.backgroundImage = url(`/static/img/midnight/midnight${number}.jpg`)

        var parts = Object.values(json)
        shuffle(parts)

        $.each(parts, function(title, values){
            var part = 
            `
            <div class="part">
                <a href="${values.link}" class="tool__item" target="_blank" rel="noopener noreferrer">
                    <img src="${values.image}" alt="${values.model}" class="part__img">
                </a>
                <h3>${values.model}</h3>
                <p class="use">${values.part}</p>                        
            </div>
            `
        $('#parts-div').append(parts)
        });
    });
});
