var data_file = document.currentScript.getAttribute('data_file0');
$(document).ready(function(){

    var music_div = `
    <div class="songs">
    `
    $.getJSON(data_file, function(json) {
        $.each(json, function(title, values){
            var style = ""
            // make an array of these albums for nowarp, same with small font

            var album_div = 
            ` 
            <div class="song__container">
                <a href="https://open.spotify.com/track/${values.id}" class="song__item">
                    <img src="${values.image}" alt="${title}" class="portfolio__img">
                <div class="song_overlay">
                    <div class="album-text">
                        <p class="song-title" style="${style}">${title}</p>
                        <p class="song-artist">${values.artists}</p>
                    </div>
                </div>
                </a>
            </div>
        </div>
        `
        music_div += album_div
        $('#songs').append(music_div)

        });

        });
});
    
       