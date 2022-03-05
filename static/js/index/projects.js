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
    $.getJSON("/data/projects.json", function(json) {

        var projects = Object.values(json)
        shuffle(projects)

        $.each(projects, function(title, values){
            if (values.title == "Goat Grade") {
                var special = `<a style="padding-left: 10px" class="project_logo" href="https://asboyer.com/blog/1" target="_blank"><i class="fas fa-book"></i></a>`
            }
            else {
                var special = ""
            }
            var project = 
            `
            <div class="project">
                <a href="${values.link}" class="project__item" target="_blank" rel="noopener noreferrer">
                    <img src="${values.image}" alt="${values.title}" class="project__img">
                </a>
                <h3>${values.title}</h3>
                <a class="project_logo" href="${values.github}" target="_blank"><i class="fab fa-github fa-lg" aria-hidden="true"></i></a>
                ${special}
            </div>
            `
        $('#projects-div').append(project)
        });
    });
});
