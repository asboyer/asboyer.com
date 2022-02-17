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
    $.getJSON("/data/podcasts.json", function(json) {

        var stories = Object.values(json)
        shuffle(stories)
        stories.sort((a,b) => (a.start_date < b.start_date) ? 1 : ((b.start_date < a.start_date) ? -1 : 0))

        $.each(stories, function(title, values){

            var story = 
            `
            <div class="news__container">
                <a href="${values.link}" target="_blank" class="news__item">
                    <img src="${values.img}" alt="${values.title}" class="blog__img">
                    <div class="news_overlay">
                        <div class="news-text">
                            <p class="news-title">${values.title}</p>
                            <p class="publication">Seasons: ${values.seasons}</p>
                            <p class="news-date">Episodes: ${values.episodes}</p>
                        </div>
                    </div>
                </a>
            </div>
            `
        $('#all_news').append(story)
        });
    });
});
