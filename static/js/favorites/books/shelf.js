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
    $.getJSON(data_file, function(json) {

        var books = Object.values(json)
        shuffle(books)

        



        $.each(books, function(title, values){
            var movie_div = 
            `
            <div class="book__container" style="background-color: ${values.color}">
                <a href="${values.link}" class="book__item" target="_blank">
                    <img src="${values.img}" alt="${values.title}" id=${values.img} class="portfolio__img">
                <div class="book_overlay">
                    <div class="book-text">
                        <p class="book-title">${values.title}</p>
                        <p class="author">${values.author}</p>
                    </div>
                </div>
                </a>
            </div>
            `
            // <p class="artist" style="font-size: 10px">${values.asboyer_score}</p>

        $('#books_div').append(movie_div)

        });
    });

});
