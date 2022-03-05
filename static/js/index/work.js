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

    var month = new Array();
    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";

    $.getJSON("/data/work.json", function(json) {

        var jobs = Object.values(json)
        jobs.sort((a,b) => (a.start_date < b.start_date) ? 1 : ((b.start_date < a.start_date) ? -1 : 0))
        jobs = jobs.slice(0, 3)

        jobs.sort(function(a, b) {
            if(a.end_date.toLowerCase() == "present") return -1;
            else if(b.end_date.toLowerCase() == "present") return 1;
            else return a - b;
        });

        jobs.sort(function(a, b) {
            if (a.end_date.toLowerCase() == "present" && b.end_date.toLowerCase() == "present") {
                if(a.start_date < b.start_date) return 1;
                else if(b.start_date < a.start_date) return -1;
            }
            else {
                return 0;
            }
        });

        $.each(jobs, function(title, values){

            var roles = Object.values(values.roles)
            if(values.roles.length != 1){
                roles.sort((a,b) => (a.start_date < b.start_date) ? 1 : ((b.start_date < a.start_date) ? -1 : 0))
            }
            var role = roles[0]


            if(values.end_date.toLowerCase() != "present"){
                var dates = values.end_date.split("-")
                var end_date = new Date(parseInt(dates[0]), parseInt(dates[1]), parseInt(dates[2]));
                var end_string = month[end_date.getMonth() - 1] + " " + end_date.getFullYear()
            }
            else {
                var end_string = "Present"
            }
            var dates = values.start_date.split("-")
            var start_date = new Date(parseInt(dates[0]), parseInt(dates[1]), parseInt(dates[2]));
            var start_string = month[start_date.getMonth()  - 1] + " " + start_date.getFullYear()

            var job = 
            `
            <div class="job">

                <a href="${values.website}" class="job__item" target="_blank" rel="noopener noreferrer">
                    <img src="${values.image}" alt="${values.company}" class="job__img">
                </a>
                <h3>${role.role}</h3>
                <div class="job__description">
                    <p>${role.description}
                       <br>
                       <br>
                       <em>${start_string} - ${end_string}</em>
                    </p>
                </div>

            </div>
            `
        $('#work').append(job)
        });
    });
});
