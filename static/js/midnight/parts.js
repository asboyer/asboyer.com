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
    $.getJSON("/data/tools.json", function(json) {

        var tools = Object.values(json)
        shuffle(tools)

        $.each(tools, function(title, values){
            var tool = 
            `
            <div class="tool">
                <a href="${values.link}" class="tool__item" target="_blank" rel="noopener noreferrer">
                    <img src="${values.image}" alt="${values.use}" class="tool__img">
                </a>
                <h3>${values.tool}</h3>
                <p class="use">${values.use}</p>                        
            </div>
            `
        $('#tools-div').append(tool)
        });
    });
});
