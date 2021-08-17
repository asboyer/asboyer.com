$(document).ready(function(){

    var music_div = `
    <div class="all-albums">
    `
    $.getJSON("/data/music_all_time.json", function(json) {
        $.each(json, function(title, values){
            var album_div = 
            `
        <div class="all-album__container">
            <a href="https://open.spotify.com/album/${values.id}" target="_blank" class="album__item">
                <img src="${values.image}" alt="${title}" class="portfolio__img">
            <div class="album_overlay">
                <div class="album-text">
                    <p class="title">${title}</p>
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
