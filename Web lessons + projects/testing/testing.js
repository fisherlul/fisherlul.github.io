let news_div = document.querySelector(".news_div")

fetch(`https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
    .then(res => res.json())
    .then((data) => {
        news_div.innerHTML = "";

        for (let i = 0; i < 1; i++) {
            let html = `<article>
                <div>
                    <h2>${data['results'][i]['title']}</h2>
                    <p>${data['results'][i]['byline']}</p>
                    <a href = "${data['results'][i]['url']}">Read More <span>>></span></a>
                </div>
            </article>`

            news_div.innerHTML += html;
        }
    })

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

// let click_count = 0
// let validate = 0
// addEventListener("click", function() {
//     click_count += 1;

//     if (click_count % 2 != 0) {
//         validate = true
//     } else if (click_count % 2 == 0) {
//         validate = false
//     }

//     if(validate = true) {
//         console.log("Liked")
//     } else {
//         console.log("Disliked")
//     }

// });
var liked = false;
var disliked = false;
var btn1 = document.querySelector('#green');
var btn2 = document.querySelector('#red');

btn1.addEventListener('click', function () {

    if (btn2.classList.contains('red')) {
        btn2.classList.remove('red');
    }
    this.classList.toggle('green');
    
    // one-click-only button
    if (!liked) {
        liked = true;
        alert('liked!')
        console.log(liked);
    }
});

btn2.addEventListener('click', function () {

    if (btn1.classList.contains('green')) {
        btn1.classList.remove('green');
    }
    this.classList.toggle('red');
    
    // one-click-only button
    if (!disliked) {
        disliked = true;
        alert('disliked!')
        console.log(disliked);
    }
});


