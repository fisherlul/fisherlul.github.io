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

let getDataNews = () => {
    fetch(`https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
    .then(res=> res.json())
    .then((data)=> {
        // news_div.textContent = data['results'][0]['abstract']
        console.log(data)
        // console.log(news_div)
        news_div.innerHTML = "";
        main_news_div.innerHTML = "";

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
        main_news_div.innerHTML += html;
    })


};
getDataNews()

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

let getMainNews = () => {
    fetch(`https://api.nytimes.com/svc/topstories/v2/home.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
    .then(res=> res.json())
    .then((data)=> {
        // news_div.textContent = data['results'][0]['abstract']
        console.log(data)
        // console.log(news_div)
        main_news_div.innerHTML = "";

        for (let i = 0; i < 10; i++) {
            let html = `
                <article class="article ${i}">
                    <img src="${data['results'][i]['multimedia'][0]['url']}"></img>
                    <h1>${data['results'][i]['title']}</h1>
                </div>`
            if (i == 8 && i == 9) {
                let html = `
                <article class="article ${i}">
                    <img src="${data['results'][i]['multimedia'][0]['url']}"></img>
                    <h1>${data['results'][i]['title']}</h1>
                    <h2>${data['results'][i]['abstract']}</h2>
                </div>`
            }
            
            main_news_div.innerHTML += html;
        }
    })
};

getMainNews()


// let mixData = (data, l) => {
//     let newsData = []
//     let keyData = ["1001002", "1001005", "1001006", "1001007", "1001009", "1001011"]
//     for (let i = 0; i < l; i++) {
//         let topicIndex = keyData[getRandomInt(0, keyData.length)]
//         let newsIndex = getRandomInt(0, 7)

//         newsData.push(data[topicIndex].data[newsIndex])
//     }
//     return newsData
// }

// let renderDataNews = (data, query) => {
//     let domSide = document.querySelector(query)
//     domSide.innerHTML = "";
//     for (let i = 0; i < data.length; i++) {
//         let html = `<article>
//         <img src = "${data[i].thumbnail_url}">
//         <div>
//             <h3>${data[i].title}</h3>
//             <p>${data[i].lead}</p>
//             <a href = "#">Read More <span>>></span></a>
//         </div>
//     </article>`

//         domSide.innerHTML += html;
//     }
// };

// let renderJustIn = (data, query) => {
//     let domJustIn = document.querySelector("#just-in")
//     domJustIn.innerHTML = "";
//     for (let i = 0; i < data.length; i++) {
//         let html = `<article>
//         <h4>just in</h4>
//         <div>
//             <h2>${data[i].title}</h2>
//             <p>${data[i].lead}</p>
//             <a href = "#">Read More <span>>></span></a>
//         </div>
//         <img src = "${data[i].thumbnail_url}">
//     </article>`

//         domJustIn.innerHTML += html;
//     }
// }

// let renderHotNews = (data) => {
//     let domHotNews = document.querySelector("#hot-news")
//     domHotNews.innerHTML = "";
//     for (let i = 0; i < data.length; i++) {
//         let html = ` <div class="hot-topic">
//         <img src = "${data[i].thumbnail_url}">
//         <div class="hot-topic-content">
//             <h1>${data[i].title}</h1>
//             <p>${data[i].lead}</p>
//             <a href="#">Read more..</a>
//         </div>
//     </div>`
//         domHotNews.innerHTML += html;
//     }
// }

// let renderCurrentNews = (data) => {
//     let domCurrentNews = document.querySelector("#current-news")
//     domCurrentNews.innerHTML = "";
//     for (let i = 0; i < data.length; i++) {
//         let html = `<h3>${data[i].title} <span>${data[i].article_category.cate_name}</span></h3> `
//         domCurrentNews.innerHTML += html;
//     }
// }

// function getRandomInt(min, max) {
//     min = Math.ceil(min);
//     max = Math.floor(max);
//     return Math.floor(Math.random() * (max - min) + min);
// }


