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
        
        const years = new Set()

        $.each(books, function(title, values){
            years.add(values.year)
        });

        let yrs = Array.from(years);
        yrs.sort().reverse()
        for (const year of yrs) {

            year_div = `
            <section class="my-current-books" style="border-top: none;">
            <div class="title-book" style="">
                        <p class="section__subtitle section__subtitle--books">${year}</p>
                        </div>
                        <div class="books">`

            $.each(books, function(title, values){

                if (values.year == year) {
                year_div += 
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
                }
            });
            year_div += `</div></section>`
            $('#current-books').append(year_div)
        }

    });

});
