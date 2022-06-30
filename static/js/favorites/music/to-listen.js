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
        shuffle(albums)

        $.each(albums, function(title, values){

            var styles = ""
            // make an array of these albums for nowarp, same with small font
            if(values.name == "T R A P S O U L" || values.name == "A N N I V E R S A R Y") {
                styles = "white-space: nowrap"
            }

            if(values.name == "Future & Juice WRLD Present... WRLD ON DRUGS") {
                styles = "font-size: 20px"
            }
            var link = `https://open.spotify.com/album/${values.id}`
            if(values.uri == "") {
                link = values.id
            }

            var album_div = 
            `
        <div class="all-album__container">
            <a href="${link}" target="_blank" class="album__item">
                <img src="${values.image}" alt="${values.name}" class="portfolio__img">
            <div class="album_overlay">
                <div class="album-text">
                    <p class="title" style="${styles}">${values.name.split("(O")[0].split("(M")[0].split("(2")[0].split("(T")[0].split("(C")[0].split("(E")[0].replace("- The Complete Edition", "").replace(" [Deluxe Edition]", "").replace("(Deluxe)", "").replace("(Remastered)", "").replace("(Original Motion Picture Soundtrack)", "").replace("(Legacy Edition)", "")}</p>
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
