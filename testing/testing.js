let news_div = document.querySelector(".news_div")

fetch(`https://skysportsapi.herokuapp.com/sky/getnews/football/v1.0/`)
    .then(res=> res.json())
    .then((data)=> {
        // news_div.textContent = data['results'][0]['abstract']
        console.log(data)
        // console.log(news_div)
        // news_div.innerHTML = "";

        // for (let i = 0; i < 4; i++) {
        //     let html = `<article>
        //         <div>
        //             <h3>${data['results'][i]['abstract']}</h3>
        //             <p>${data['results'][i]['byline']}</p>
        //             <a href = "${data['results'][i]['url']}">Read More <span>>></span></a>
        //         </div>
        //     </article>`

        //     news_div.innerHTML += html;
        // }
    })

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}


