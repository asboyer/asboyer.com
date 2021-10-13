var data_file0 = document.currentScript.getAttribute('data_file0');

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
    console.log(data_file0)
    var music_div = `
    <div class="songs">
    `
    $.getJSON(data_file0, function(json) {

        var songs = Object.values(json)
        songs.sort((a,b) => (a.popularity < b.popularity) ? 1 : ((b.popularity < a.popularity) ? -1 : 0))
        shuffle(songs)

        $.each(songs, function(title, values){
            var style = ""
            // make an array of these albums for nowarp, same with small font
            // check length of title and then add special css
            var album_div = 
            ` 
            <div class="song__container">
                <a href="https://open.spotify.com/track/${values.id}" class="song__item">
                    <img src="${values.image}" alt="${values.name}" class="portfolio__img">
                <div class="song_overlay">
                    <div class="album-text">
                        <p class="song-title" style="${style}">${values.name.split('(')[0].split(' (with')[0].split(' (Main')[0].split("- From")[0]}</p>
                        <p class="song-artist">${values.artists}</p>
                    </div>
                </div>
                </a>
            </div>
        `

        music_div += album_div

        });
        music_div += `
        </div>
        `
        $('#songs').append(music_div)

        });
});
    
       