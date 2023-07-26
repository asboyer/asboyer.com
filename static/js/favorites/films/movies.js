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
        movies.sort((a,b) => (a.rating < b.rating) ? 1 : ((b.rating < a.rating) ? -1 : 0))
        shuffle(movies)
        movies.sort((a,b) => (a.stars < b.stars) ? 1 : ((b.stars < a.stars) ? -1 : 0))

        
        // movies.sort((a,b) => (a.asboyer_score < b.asboyer_score) ? 1 : ((b.asboyer_score < a.asboyer_score) ? -1 : 0))

        $.each(movies, function(title, values){


            var half_star = false
            if (parseInt(values.stars) < values.stars) {
                half_star = true;
            }

            var star_string = ""
            for (var i = 0; i < parseInt(values.stars); i++) {
                star_string += `<i class="fas fa-star"></i>`
            }
            if (half_star) {
                star_string += `<i class="fas fa-star-half"></i>`
            }

            var movie_div = 
            `
            <div class="movie__container">
                <a href="https://www.imdb.com/title/tt${values.id}/" target="_blank" class="movie__item">
                    <img src="${values.image}" alt="${values.title}" class="portfolio__img">
                <div class="movie_overlay">
                    <div class="movie-text">
                        <p class="movie-title">${values.title}</p>
                        <p class="artist">${values.director}</p>
                        <p class="author">${star_string}</p>
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
        <p id="letterp">---<br><a href="https://letterboxd.com/asboyer/" target="_blank" id="letterboxd">letterboxd</a></p>

        `
        $('#movies').append(movies_div)
    });

});
