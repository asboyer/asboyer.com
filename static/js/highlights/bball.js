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
    $.getJSON("/data/highlights/bball_2022.json", function(json) {
        var stories = Object.values(json)
        shuffle(stories)
        stories.sort((a,b) => (a.date < b.date) ? 1 : ((b.date < a.date) ? -1 : 0))
        $.each(stories, function(title, values){
            var str = values.date.split("-")
            var date_string = str[1]
            date_string += "."
            if (str[2].substring(0, 1) == '0') {date_string += str[2].substring(1, 2)
            }
            else {date_string += str[2]}
            date_string += "."
            date_string += str[0].substring(2, 4)
            var game = 
            `
            <div class="iframe_container">
                <div style="text-align: center">
                    <p class="game-text">${values.opponent}</p>
                    <p class="game-text-date">${date_string}</p>
                </div>
                <iframe class="responsive-iframe" allowfullscreen
                src="${values.link}">
                </iframe>
            </div>
            `
        $('#all_games').append(game)
        });
    });
});
