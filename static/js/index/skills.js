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
    $.getJSON("/data/skills.json", function(json) {

        var skills = Object.values(json)
        skills.sort((a,b) => (a.order > b.order) ? 1 : ((b.order > a.order) ? -1 : 0))

        $.each(skills, function(title, values){
            var skill = 
            `
            <div class="service">
                <i class="${values.img}"></i>
                <h3>${values.title}</h3>
                <p>${values.body}</p>
            </div>
            `
        $('#skills-div').append(skill)
        });
    });
});
