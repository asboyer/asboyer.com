var data_file0 = document.currentScript.getAttribute('data_file0');
$(document).ready(function(){
    console.log(data_file0)
    var music_div = `
    <div class="songs">
    `
    $.getJSON(data_file0, function(json) {
        $.each(json, function(title, values){
            var style = ""
            // make an array of these albums for nowarp, same with small font
            // check length of title and then add special css
            var album_div = 
            ` 
            <div class="song__container">
                <a href="https://open.spotify.com/track/${values.id}" class="song__item">
                    <img src="${values.image}" alt="${title}" class="portfolio__img">
                <div class="song_overlay">
                    <div class="album-text">
                        <p class="song-title" style="${style}">${title.split(' (feat')[0].split(' (with')[0]}</p>
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
    
       