

const btnHam = document.querySelector('.ham-btn');
const btnTime = document.querySelector('.time-btn');
const navBar = document.getElementById('nav-bar');

btnHam.addEventListener('click', function(){
    if(btnHam.className !== ""){
        btnHam.style.display  = "none";
        btnTime.style.display = "block";
        navBar.classList.add("show-nav");
    }
})

btnTime.addEventListener('click', function(){
    if(btnHam.className !== ""){
        this.style.display = "none";
        btnHam.style.display = "block";
        navBar.classList.remove("show-nav");
    }
});
;

let getDataNews = async ()=>{
    let draw = await fetch('https://vnexpress.net/microservice/home');
    let data = await draw.data;

    renderDataNews(mixData(data.data))
};

// let getDataInfo = async ()=>{
//     let draw = await fetch('https://vnexpress.net/microservice/home')
//     let data = await draw.data
// }
let mixData = (data)=>{
    let newData = []
    let keyData = ["1001002", "1001005", "1001006", "1001007", "1001009", "1001011"]
    for(let i= 0; i< 10; i++){
        let topicIndex = keyData[getRandomInt(0, keyData.length)]
        let newsIndex = getRandomInt(0, 7) 

        newData.push(data[topicIndex].data[newsIndex])
    }

    return newData
}

let renderDataNews = (data)=>{
    let dom= document.querySelector("#a")
    dom.innerHTML = "";
    for(let i=0; i<data.length; i++){
        let html = `<article>
        <img src = "images/bottom-left-2.jpg">
        <div>
            <h3>iPad Pro, reviewed: Has the iPad become my main computer now?</h3>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Commodi iure modi animi cupiditate. Explicabo, nihil?</p>

            <a href = "#">Read More <span>>></span></a>
        </div>
    </article>`

    dom.innerHTML += html;
    }
};
getDataNews();

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
  }