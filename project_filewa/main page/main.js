import { initializeApp } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-firestore.js";
import { doc, setDoc, addDoc, collection, updateDoc } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-firestore.js";
const firebaseConfig = {
    apiKey: "AIzaSyCfZZS6UMhmouh_RwBK3ItKnsP7hQYLuYQ",
    authDomain: "the-real-daily-bugle.firebaseapp.com",
    projectId: "the-real-daily-bugle",
    storageBucket: "the-real-daily-bugle.appspot.com",
    messagingSenderId: "806795679544",
    appId: "1:806795679544:web:3d95df4ce0d6cee13253cd",
    measurementId: "G-LBJ3RHGWS5"
};


// Minimize the windows
const btnHam = document.querySelector('.ham-btn');
const btnTimes = document.querySelector('.times-btn');
const navBar = document.getElementById('nav-bar');

btnHam.addEventListener('click', function () {
    if (btnHam.className !== "") {
        btnHam.style.display = "none";
        btnTimes.style.display = "block";
        navBar.classList.add("show-nav");
    }
})

btnTimes.addEventListener('click', function () {
    if (btnHam.className !== "") {
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
    fetch(`https://api.nytimes.com/svc/topstories/v2/world.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
        .then(res => res.json())
        .then((data) => {
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
                <div>
                    <button class="btn-button 1" id="green"><i class="fa fa-thumbs-up fa-lg" aria-hidden="true"></i></button>
                    <button class="btn-button 2" id="red"><i class="fa fa-thumbs-down fa-lg" aria-hidden="true"></i></button>
                </div>
            </article>`

                news_div.innerHTML += html;

            }
        })


};
getDataNews()

let getSideNews = () => {
    fetch(`https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
        .then(res => res.json())
        .then((data) => {
            // news_div.textContent = data['results'][0]['abstract']
            console.log(data)
            // console.log(news_div)
            side_news_div.innerHTML = "";

            for (let i = 1; i < 5; i++) {
                let html = `<article class="just-in">
                <div class="just-in-news">
                    <h2>${data['results'][getRandomInt(0, i)]['abstract']}</h2>
                    <a href = "${data['results'][getRandomInt(0, i)]['url']}">Read More <span>>></span></a>
                </div>
                <div>
                    <button class="btn-button 1" id="green"><i class="fa fa-thumbs-up fa-lg" aria-hidden="true"></i></button>
                    <button class="btn-button 2" id="red"><i class="fa fa-thumbs-down fa-lg" aria-hidden="true"></i></button>
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
    fetch(`https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=8e4wCNCI0dajNRR5mfAc4GGlmqmxGE9Y`)
        .then(res => res.json())
        .then((data) => {
            // news_div.textContent = data['results'][0]['abstract']
            console.log(data)
            // console.log(news_div)
            main_news_div.innerHTML = "";
            for (let i = 0; i < 1; i++) {
                let html = `
                <article class="article">
                    <img src="${data['results'][i]['multimedia'][2]['url']}"></img>
                    <h1>${data['results'][i]['title']}</h1>
                </article>
                `
                main_news_div.innerHTML += html;
            }
        })
};

getMainNews()

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getFirestore(app) 

const btn1 = document.getElementById('green');
const btn2 = document.getElementById('red');

const docTest = await addDoc(collection(database, "testing 2"), {
    liked: false, 
    disliked: false,
    testing: "123"
});

console.log(docTest.id);

btn1.addEventListener('click', function onClick() {

    if (btn2.classList.contains('red')) {
        btn2.classList.remove('red');
    }
    this.classList.toggle('green');
    // updateDoc(db, "likes-dislikes", "testing", "news", "news", {
    //     disliked: false,
    //     liked: true
    // });

    console.log("Hello")

});

btn2.addEventListener('click', function onClick() {

    if (btn1.classList.contains('green')) {
        btn1.classList.remove('green');
    }
    this.classList.toggle('red');
    // updateDoc(db, "likes-dislikes", "news", "news", {
    //     disliked: true,
    //     liked: false
    // });
    console.log("Bye")

});