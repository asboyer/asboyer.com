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

            var post = 
            `
            <div class="blog__container">
                <a href="/blog/${values.id}" class="blog__item">
                    <img src="/static/img/l.png" alt="${values.title}" class="blog__img">
                    <div class="overlay">
                        <div class="text">
                            <p class="title">${values.title}</p>
                            <p class="date">${date_string}</p>
                            <p class="subject">${subject_str}</p>
                        </div>
                    </div>
                </a>
            </div>
            `
            $('#posts').append(post)
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

        posts = posts.splice(0, pub_posts)

        $.each(posts, function(title, values){

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

            var post = 
            `
            <div class="blog__container">
                <a href="/blog/${values.id}" class="blog__item">
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
        });

    });
});

