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

    // $.getJSON(data_file, function(json) {
    $.getJSON(data_file, function(json) {

        var albums = Object.values(json)
        albums.sort((a,b) => (a.popularity < b.popularity) ? 1 : ((b.popularity < a.popularity) ? -1 : 0))
        shuffle(albums)
        albums.sort((a,b) => (a.score < b.score) ? 1 : ((b.score < a.score) ? -1 : 0))


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
            var artist_length = ""
            var title_length = ""
            var styles = ""
            // if(values.name == "The Search" || values.name == "Whole Lotta Red" || values.name == "From Me To You" || values.name == "The College Dropout" || values.name == "Thats What They All Say") {
            //     tracklist += '-long'
            // }
            // // do something special if just one album
            // if(values.name == "Donda" || values.name == "The Life Of Pablo" || values.name == "Scorpion") {
            //     tracklist += '-rlong'
            //     artist_length = "-long"
            //     title_length = "-long"
            // }
            track_style = ""
            top_tracks = false
            if (values.top_tracks.length == 0) top_tracks = true;
            if(top_tracks){
                track_style = "display: none;"
            }
            if (values.name == "In The Court Of The Crimson King (Expanded & Remastered Original Album Mix)") track_style = "white-space: wrap;";
            if (values.name == "Donda 2") {
                link = "/qban2"
            }
            else if (values.uri == "") {
                link = values.id
            }
            else {
                link = `https://open.spotify.com/album/${values.id}`
            }
            if(values.name == "T R A P S O U L" || values.name == "A N N I V E R S A R Y" || values.name == "JuiceWRLD 9 9 9") {
                styles = "white-space: nowrap"
            }
            var special = ""
            if(values.name == "So Much Fun (Deluxe)" || values.name == "WUNNA (Deluxe)") {
                special = " (Deluxe)"
            }


            // make an array of these albums for nowarp, same with small font
            if (values.score == null) values.score = ""
            if (values.score == 0.0) values.score = ""
            var album_div =
            `<div class="album__container">
            <a href="${link}" class="album__item" target="_blank">
                <img src="${values.image}" alt="${values.name}" class="portfolio__img">
            <div class="album_overlay">
                <div class="album-text">
                    <p class="title${title_length}" style="${styles}">${values.name.split("(")[0].replace("(Deluxe)", "").replace("(Remastered)", "").replace("(Original Motion Picture Soundtrack)", "").replace("(Legacy Edition)", "").replace(" (Platinum VIP Edition)", "").replace(" (Original Television Series Soundtrack)", "").replace(" [Deluxe Edition]", "").split(" (Original")[0] + special}</p>
                    <p class="artist${artist_length}">${values.artists}</p>
                    <p class="artist" style="${track_style}; font-size: 10px"=>${values.score}</p>
                    <div class="the-tracks" style="${track_style}">
                        <ul class="tracklist${tracklist}">
                        <li class="tracks${tracklist}">A Few Top Tracks:</li>
            `
            var track_list = ''
            top_tracks = values.top_tracks
            shuffle(top_tracks)
            if (top_tracks.length > 3){
                top_tracks = top_tracks.slice(0, 4)
            }
            for (let i = 0; i < top_tracks.length; i++) {
                track_list += `
                            <li>${top_tracks[i].split("(feat")[0].split("(with")[0].split("- Including")[0]}</li>
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
