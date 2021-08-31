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
    var music_div = `
    <div class="all-albums">
    `
    $.getJSON(data_file, function(json) {

        var albums = Object.values(json)
        albums.sort((a,b) => (a.popularity < b.popularity) ? 1 : ((b.popularity < a.popularity) ? -1 : 0))
        shuffle(albums)

        $.each(albums, function(title, values){

            var styles = ""
            // make an array of these albums for nowarp, same with small font
            if(values.name == "T R A P S O U L") {
                styles = "white-space: nowrap"
            }

            if(values.name == "Future & Juice WRLD Present... WRLD ON DRUGS") {
                styles = "font-size: 20px"
            }

            var album_div = 
            `
        <div class="all-album__container">
            <a href="https://open.spotify.com/album/${values.id}" target="_blank" class="album__item">
                <img src="${values.image}" alt="${values.name}" class="portfolio__img">
            <div class="album_overlay">
                <div class="album-text">
                    <p class="title" style="${styles}">${values.name.split("(Original")[0].replace(" [Deluxe Edition]", "").replace("(Deluxe)", "").replace("(Remastered)", "").replace("(Original Motion Picture Soundtrack)", "").replace("(Legacy Edition)", "")}</p>
                    <p class="artist">${values.artists}</p>
                </div>
            </div>
            </a>
        </div>
            `

        music_div = music_div + album_div
        });
        music_div = music_div + `
        </div>
        `
        $('#albums').append(music_div)

    });

});
