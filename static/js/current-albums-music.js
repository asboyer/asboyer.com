$(document).ready(function(){

    var music_div = `
    <div class="all-albums">
    `
    $.getJSON("/data/music_all_time.json", function(json) {
        $.each(json, function(title, values){

            var styles = ""
            // make an array of these albums for nowarp, same with small font

            var album_div = 
            `<div class="album__container">
            <a href="https://open.spotify.com/album/${values.id}" class="album__item">
                <img src="${values.image}" alt="${title}" class="portfolio__img">
            <div class="album_overlay">
                <div class="album-text">
                    <p class="title" style="${styles}">${title.replace("(Deluxe)", "").replace("(Remastered)", "").replace("(Original Motion Picture Soundtrack)", "").replace("(Legacy Edition)", "").replace(" (Platinum VIP Edition)", "")}</p>
                    <p class="artist">${values.artists}</p>
                    <div class="the-tracks">
                        <ul class="tracklist">
                        <li class="tracks">Top Tracks:</li>
            `
            var track_list = ''
            for (int i = 0; i < values.top_tracks.length; i++) {
                track_list += `
                            <li>${valus.top_tracks[i]}</li>
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

    });

});
