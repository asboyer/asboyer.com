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
        albums.sort((a,b) => (a.date < b.date) ? 1 : ((b.date < a.date) ? -1 : 0))

        $.each(albums, function(title, values){

            var date_str = values.date.split('-')
            if(date_str[1].startsWith('0')) {
                date_str[1] = date_str[1].replace('0', '') 
            
            }
            if(date_str[2].startsWith('0')) {
                date_str[2] = date_str[2].replace('0', '') 
            }   
            var date = date_str[1] + "." + date_str[2] + "." + date_str[0].substring(2, 4)

            var caption = ""

            if(values.caption != "") {
                caption = `<p style="font-size: 18px; font-weight: bold" class="song-artist">${values.caption}</p>`
            }
            else {
                caption = `<p style="font-size: 18px; font-weight: bold" class="song-artist">${(values.name).split(".")[0]}</p>`
            }

            var link = `/static/img/gallery/${values.name}`

            if(values.link != "") {
                link = values.link
            }


            var album_div =
            `

        <div class="all-album__container">
            <a href="${link}" target="_blank" class="album__item">

                <img src="/static/img/gallery/${values.name}" alt="${values.name}" class="gallery__img">
            <div class="album_overlay">
                <div class="album-text">
                        ${caption}
                        <p class="song-artist">${date}</p>
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

