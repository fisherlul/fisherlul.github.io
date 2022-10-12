// Minimize the windows
const btnHam = document.querySelector('.ham-btn');
const btnTimes = document.querySelector('.times-btn');
const navBar = document.getElementById('nav-bar');

btnHam.addEventListener('click', function(){
    if(btnHam.className !== ""){
        btnHam.style.display = "none";
        btnTimes.style.display = "block";
        navBar.classList.add("show-nav");
    }
})

btnTimes.addEventListener('click', function(){
    if(btnHam.className !== ""){
        this.style.display = "none";
        btnHam.style.display = "block";
        navBar.classList.remove("show-nav");
    }
})
// Render, mix and get news data
const news_div = document.getElementById('main-news')
const main_news_div = document.querySelector('.archive')
const side_news_div = document.querySelector('#just-in')

let getDataNews = () => {
    fetch(`https://api.nytimes.com/svc/topstories/v2/business.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
    .then(res=> res.json())
    .then((data)=> {
        console.log(data)
        // console.log(news_div)
        news_div.innerHTML = "";

        for (let i = 0; i < 4; i++) {
            let html = `<article>
                <div>
                    <h3>${data['results'][i]['abstract']}</h3>
                    <p>${data['results'][i]['byline']}</p>
                    <a href = "${data['results'][i]['url']}">Read More <span>>></span></a>
                </div>
            </article>`

            news_div.innerHTML += html;
            
        }
    })


};
getDataNews()

let getSideNews = () => {
    fetch(`https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
    .then(res=> res.json())
    .then((data)=> {
        // news_div.textContent = data['results'][0]['abstract']
        console.log(data)
        // console.log(news_div)
        side_news_div.innerHTML = "";

        for (let i = 1; i < 7; i++) {
            let html = `<article class="just-in">
                <div class="just-in-news">
                    <h2>${data['results'][i]['abstract']}</h2>
                    <a href = "${data['results'][i]['url']}">Read More <span>>></span></a>
                </div>
            </article>`

            side_news_div.innerHTML += html;
        }
    })
};

getSideNews()

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

let getMainNews = () => {
    fetch(`https://api.nytimes.com/svc/news/v3/content/nyt/business.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
    .then(res=> res.json())
    .then((data)=> {
        // news_div.textContent = data['results'][0]['abstract']
        console.log(data)
        // console.log(news_div)
        main_news_div.innerHTML = "";
        for (let i = 0; i < 10; i++) {
            let html = `
                <article class="article">
                    <img src="${data['results'][i]['multimedia'][1]['url']}"></img>
                    <h1>${data['results'][i]['title']}</h1>
                </article>`
            // if (i == 8 && i == 9) {
            //     html = `
            //     <article class="special">
            //         <img src="${data['results'][i]['multimedia'][0]['url']}"></img>
            //         <h1>${data['results'][i]['title']}</h1>
            //         <h2>${data['results'][i]['abstract']}</h2>
            //     </article>`
            // }
            main_news_div.innerHTML += html;
        }
    })
};

getMainNews()

