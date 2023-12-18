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
        albums.sort((a,b) => (a.stars < b.stars) ? 1 : ((b.stars < a.stars) ? -1 : 0))

        $.each(albums, function(title, values){

            var styles = ""
            // make an array of these albums for nowarp, same with small font
            if(values.name == "T R A P S O U L" || values.name == "A N N I V E R S A R Y" || values.name == "JuiceWRLD 9 9 9") {
                styles = "white-space: nowrap"
            }

            if(values.name == "Future & Juice WRLD Present... WRLD ON DRUGS" || values.name == "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?" || values.name == "Kanye West Presents Good Music Cruel Summer" || values.name == "Spider-Man: Into the Spider-Verse (Soundtrack From & Inspired by the Motion Picture)") {
                styles = "font-size: 20px"
            }
            var special = ""
            if(values.name == "So Much Fun (Deluxe)" || values.name == "WUNNA (Deluxe)") {
                special = " (Deluxe)"
            }

            var link = `https://open.spotify.com/album/${values.id}`
            if(values.uri == "") {
                link = values.id
            }


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

            var album_div = 
            `
        <div class="all-album__container">
            <a href="${link}" target="_blank" class="album__item">
                <img src="${values.image}" alt="${values.name}" class="portfolio__img">
            <div class="album_overlay">
                <div class="album-text">
                    <p class="title" style="${styles}">${values.name.split("(O")[0].split("(2")[0].split("(M")[0].split("(T")[0].split("(C")[0].split("(E")[0].replace("- The Complete Edition", "").replace(" [Deluxe Edition]", "").replace("(Deluxe)", "").replace("(Remastered)", "").replace("(Original Motion Picture Soundtrack)", "").replace("(Legacy Edition)", "") + special}</p>
                    <p class="artist">${values.artists}</p>
                    <p class="author">${star_string}</p>
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
