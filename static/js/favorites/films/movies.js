var data_file = document.currentScript.getAttribute('data_file');
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

    var movies_div = `
    <div class="movies">
    `
    $.getJSON(data_file, function(json) {

        var movies = Object.values(json)
        shuffle(movies)
        
        // movies.sort((a,b) => (a.asboyer_score < b.asboyer_score) ? 1 : ((b.asboyer_score < a.asboyer_score) ? -1 : 0))

        $.each(movies, function(title, values){
            var movie_div = 
            `
            <div class="movie__container">
                <a href="https://www.imdb.com/title/tt${values.id}/" target="_blank" class="movie__item">
                    <img src="${values.image}" alt="${values.title}" class="portfolio__img">
                <div class="movie_overlay">
                    <div class="movie-text">
                        <p class="movie-title">${values.title}</p>

                    </div>
                </div>
                </a>
            </div>
            `
            // <p class="artist" style="font-size: 10px">${values.asboyer_score}</p>

            movies_div = movies_div + movie_div
        });
        movies_div = movies_div + `
        </div>
        `
        $('#movies').append(movies_div)
    });

});
