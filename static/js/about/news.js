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
    $.getJSON("/data/news.json", function(json) {

        var stories = Object.values(json)
        shuffle(stories)
        stories.sort((a,b) => (a.date < b.date) ? 1 : ((b.date < a.date) ? -1 : 0))

        $.each(stories, function(title, values){
            var str = values.date.split("-")
            var date_string = str[1]
            date_string += "."
            date_string += str[2]
            date_string += "."
            date_string += str[0].substring(2, 4)
            console.log(date_string)
            var story = 
            `
            <div class="news__container">
                <a href="${values.link}" target="_blank" class="news__item">
                    <img src="${values.img}" alt="${values.title}" class="blog__img">
                    <div class="news_overlay">
                        <div class="news-text">
                            <p class="news-title">"${values.title}"</p>
                            <p class="publication">${values.publication}</p>
                            <p class="news-date">${date_string}</p>
                        </div>
                    </div>
                </a>
            </div>
            `
        $('#all_news').append(story)
        });
    });
});
