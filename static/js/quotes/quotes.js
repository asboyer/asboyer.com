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
        var quotes = Object.values(json)
        shuffle(quotes)
        quote_div = ""
        $.each(quotes, function(num, quote){
             quote_div +=
             `
             <figure class="quote_fig">
                <blockquote>
                    <p>
                    ${quote.quote}
                    </p>
                    <figcaption class="quote_author">
                    - ${quote.author}
                    </figcaption>
                </blockquote>
             </figure>
             `
        });
        $('#quotes').append(quote_div)
    });

});
