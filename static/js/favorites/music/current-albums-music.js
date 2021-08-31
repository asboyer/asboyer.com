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

console.log(data_file)
$(document).ready(function(){

    $.getJSON(data_file, function(json) {

        var albums = Object.values(json)
        albums.sort((a,b) => (a.popularity < b.popularity) ? 1 : ((b.popularity < a.popularity) ? -1 : 0))
        shuffle(albums)

        if (albums.length == 1) {
            var music_div = `
            <div class="album" id="album-div">
            `
        }
        else {
            var music_div = `
            <div class="albums" id="albums-div">
            `   
        }

        $.each(albums, function(title, values){
            var tracklist = ""
            var artist_lenth = ""
            var title_lenth = ""
            var styles = ""
            if(values.name == "From Me To You" || values.name == "The College Dropout") {
                tracklist += '-long'
            }
            // do something special if just one album
            if(values.name == "Donda") {
                tracklist += '-rlong'
                artist_length = "-long"
                title_length = "-long"
            }

            // make an array of these albums for nowarp, same with small font

            var album_div = 
            `<div class="album__container">
            <a href="https://open.spotify.com/album/${values.id}" class="album__item">
                <img src="${values.image}" alt="${values.name}" class="portfolio__img">
            <div class="album_overlay">
                <div class="album-text">
                    <p class="title${title_length}" style="${styles}">${values.name.replace("(Deluxe)", "").replace("(Remastered)", "").replace("(Original Motion Picture Soundtrack)", "").replace("(Legacy Edition)", "").replace(" (Platinum VIP Edition)", "").replace(" (Original Television Series Soundtrack)", "").replace(" [Deluxe Edition]", "").split(" (Original")[0]}</p>
                    <p class="artist${artist_length}">${values.artists}</p>
                    <div class="the-tracks">
                        <ul class="tracklist${tracklist}">
                        <li class="tracks${tracklist}">Top Tracks:</li>
            `
            var track_list = ''
            for (let i = 0; i < values.top_tracks.length; i++) {
                track_list += `
                            <li>${values.top_tracks[i]}</li>
                            `
            }
            var album_div_end = `
                        </ul>
                    </div>
                </div>
            </div>
            </a>
        </div>
        `
        
        music_div = music_div + album_div + track_list + album_div_end
        });
        music_div = music_div + `
        </div>
        `
        $('#albums').append(music_div)

        if(albums.length == 1) {

            function myFunction(x) {
                if (x.matches) { // If media query matches
                    document.getElementById('album-div').style.removeProperty('grid-template-columns')
                } 
            }

            // document.getElementById('album__container').style.maxWidth = "1000px";
            document.getElementById('album-div').style.removeProperty('grid-template-columns')
            var x = window.matchMedia("(max-width: 1400px)")
            myFunction(x)
            x.addListener(myFunction)
        }

    });

});
