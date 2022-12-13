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


function countd(month_num, day, year, time) {
    
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

    var countDownDate = new Date(`${month[month_num - 1]} ${day}, ${year} ${time}:00`).getTime();

    // Update the count down every 1 second
    var x = setInterval(function() {

    // Get today's date and time
    var now = new Date().getTime();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
    document.getElementById("clock").innerHTML = days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";

    // If the count down is over, write some text 
    if (distance < 0) {
    clearInterval(x);
    document.getElementById("clock").innerHTML = "EXPIRED";
    }
    }, 1000);
}

$(document).ready(function(){
    $.getJSON("/data/blog/posts.json", function(json) {

        var posts = Object.values(json)
        posts.sort((a,b) => (a.id < b.id) ? 1 : ((b.id < a.id) ? -1 : 0))

        if(posts.length == 2){
            document.getElementById('posts').style.maxWidth = "1000px"
        }   

        var soon_posts = []

        var p = posts.length
        while (p--) {
            if (!posts[p].live) {
                var test = posts.splice(p, 1)
                soon_posts.push(test[0])
            }
        }

        soon_posts.sort((a,b) => (a.id > b.id) ? 1 : ((b.id > a.id) ? -1 : 0))  

        // if (posts.length > 3){
        //     posts = posts.splice(0, 3)
        //     soon_posts.splice(0, soon_posts.length)
        // }
        // else if (posts.length == 2) {
        soon_posts = soon_posts.splice(0, 1)
        // }

        $.each(soon_posts, function(title, values){
            var subject_str = ""
            if (values.subjects.length == 2) {
                subject_str = values.subjects[0] + " & " + values.subjects[1]
            }
            else {  
                for (let i = 0; i < values.subjects.length; i++) {
                    if (i != values.subjects.length - 1) {
                        subject_str += values.subjects[i] + ", "
                    }
                    else {
                        subject_str += values.subjects[i]
                    }
                }
            }

            var date_string = values.date

            if (date_string == "") {
                date_string = "Coming Soon"
            }
                            
//<p class="date">${date_string}</p>
// <p class="subject">${subject_str}</p>
// <p class="date" style="font-size: 12px; font-weight: bold">${date_string}</p>
// <p class="title">${values.title}</p>

            var link = ""

            console.log(values.content_id)

            if (values.content_id > 99) {
                link = `/stories/sierra_escape/vol_${(values.content_id - 100) + 1}`
            }

            else {
                link = `/blog/${values.id}`
            }

            var type = ""

            if (values.content_id > 99) {
                type = `Sierra Escape Vol ${(values.content_id - 100) + 1}`
            }

            else {
                type = `Blog post`
            }
            var post = 
            `
            <div class="blog__container">
                <a href="${link}" class="blog__item">
                    <img src="/static/img/l.png" alt="${values.title}" class="blog__img">
                    <div class="overlay">
                        <div class="text">
                            <p class="date" style="font-family: monospace" id="clock"></p>
                            <p class="date" style="font-family: monospace; font-size: 12px">${type}</p>
                        </div>
                    </div>
                </a>
            </div>
            `
            $('#posts').append(post)
            if(date_string != "Coming Soon")
                countd(date_string.split('.')[0], date_string.split('.')[1], "20" + date_string.split('.')[2], "8:00")
        });

        // if width between 1221px and 821px, show three posts

        // still a work in progress

        // if (window.screen.width <= 1221 && window.screen.width >= 822) {
        //     var pub_posts = 3
        //     console.log('hello')
        // }

        // else {
        //     var pub_posts = 2
        // }

        pub_posts = 3

        posts = posts.splice(0, 3)

        var post_counter = 0

        $.each(posts, function(title, values){

            var style = ""
            if (post_counter == 2) {
                style = "special-cont"
            }
            var subject_str = ""

            if (values.subjects.length == 2) {
                subject_str = values.subjects[0] + " & " + values.subjects[1]
            }
            else {  
                for (let i = 0; i < values.subjects.length; i++) {
                    if (i != values.subjects.length - 1) {
                        subject_str += values.subjects[i] + ", "
                    }
                    else {
                        subject_str += values.subjects[i]
                    }
                }
            }
            var link = ""

            console.log(values.content_id)

            if (values.content_id > 99) {
                link = `/stories/sierra_escape/vol_${(values.content_id - 100) + 1}`
            }

            else {
                link = `/blog/${values.id}`
            }

            var post = 
            `
            <div class="blog__container" id="${style}">
                <a href="${link}" class="blog__item">
                    <img src="${values.cover_img}" alt="${values.title}" class="blog__img">
                    <div class="overlay">
                        <div class="text">
                            <p class="title">${values.title}</p>
                            <p class="date">${values.date}</p>
                            <p class="subject">${subject_str}</p>
                        </div>
                    </div>
                </a>
            </div>
            `
            $('#posts').append(post)
            post_counter += 1
        });

    });
});

