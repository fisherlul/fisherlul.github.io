

let getDataNews = async () => {
    try {
        const response = await axios.get(
            "https://vnexpress.net/microservice/home"
        );
        let data = await response.data;
        console.log(data);
        renderDataNews(mixData(data.data, 1), "#main-news")
        renderDataNews(mixData(data.data, 4), "#side-news")
        renderJustIn(mixData(data.data, 4))
        renderHotNews(mixData(data.data, 4))
    } catch (error) {
        console.error(error);
    }

    // renderDataNews(mixData(data.data))
};
getDataNews()

// let getDataInfo = async ()=>{
//     let draw = await fetch('https://vnexpress.net/microservice/home')
//     let data = await draw.data
// }
let mixData = (data, l) => {
    let newData = []
    let keyData = ["1001002", "1001005", "1001006", "1001007", "1001009", "1001011"]
    for (let i = 0; i < l; i++) {
        let topicIndex = keyData[getRandomInt(0, keyData.length)]
        let newsIndex = getRandomInt(0, 7)

        newData.push(data[topicIndex].data[newsIndex])
    }

    return newData
}

let renderDataNews = (data, query) => {
    let domSide = document.querySelector(query)
    domSide.innerHTML = "";
    for (let i = 0; i < data.length; i++) {
        let html = `<article>
        <img src = "${data[i].thumbnail_url}">
        <div>
            <h3>${data[i].title}</h3>
            <p>${data[i].lead}</p>
            <a href = "#">Read More <span>>></span></a>
        </div>
    </article>`

        domSide.innerHTML += html;
    }
};

let renderJustIn = (data, query) => {
    let domJustIn = document.querySelector("#just-in")
    domJustIn.innerHTML = "";
    for (let i = 0; i < data.length; i++) {
        let html = `<article>
        <h4>just in</h4>
        <div>
            <h2>${data[i].title}</h2>
            <p>${data[i].lead}</p>
            <a href = "#">Read More <span>>></span></a>
        </div>
        <img src = "${data[i].thumbnail_url}">
    </article>`

        domJustIn.innerHTML += html;
    }
}

let renderHotNews = (data) => {
    let domHotNews = document.querySelector("#hot-news")
    domHotNews.innerHTML = "";
    for (let i = 0; i < data.length; i++) {
        let html = ` <div class="hot-topic">
        <img src = "${data[i].thumbnail_url}">
        <div class="hot-topic-content">
            <h1>${data[i].title}</h1>
            <p>${data[i].lead}</p>
            <a href="#">Read more..</a>
        </div>
    </div>`
        domHotNews.innerHTML += html;
    }
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

// CURRENCY TABLE
// fetch cryptocurrency data and store it in the variable data
var xhReq = new XMLHttpRequest();
xhReq.open("GET", "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd", false);
xhReq.send(null);
var data = JSON.parse(xhReq.responseText);

// initialization
var cryptocurrencies;
var timerId;
var updateInterval = 30000;


function ascending(a, b) { return a.percent_change_24h > b.percent_change_24h ? 1 : -1; }
function descending(a, b) { return a.percent_change_24h < b.percent_change_24h ? 1 : -1; }
function reposition() {
    var height = $("#cryptocurrencies .cryptocurrency").height();
    var y = height;
    for (var i = 0; i < cryptocurrencies.length; i++) {
        cryptocurrencies[i].$item.css("top", y + "px");
        y += height;
    }
}
function updateRanks(cryptocurrencies) {
    for (var i = 0; i < cryptocurrencies.length; i++) {
        cryptocurrencies[i].$item.find(".rank").text(i + 1);
    }
}

function fetchNewData(data, attributeName, name) {
    for (var x in data) {
        if ((data[x].name == name) == true) {
            return data[x][attributeName];
        }
    }
    return null;
}
function updateBoard() {
    var cryptocurrency = getRandomCoin();
    cryptocurrency.percent_change_24h += getRandomScoreIncrease();
    cryptocurrency.$item.find(".percent_change_24h").text(cryptocurrency.percent_change_24h);
    cryptocurrencies.sort(descending);
    updateRanks(cryptocurrencies);
    reposition();
}

function getNewData() {
    // get the new data for each coin and change to their new values
    var newReq = new XMLHttpRequest();
    newReq.open("GET", "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd", false);
    newReq.send(null);
    var newData = JSON.parse(newReq.responseText);

    for (var i = 0; i < cryptocurrencies.length; i++) {
        var cryptocurrency = cryptocurrencies[i];
        cryptocurrency.price = fetchNewData(newData, 'current_price', cryptocurrency.name);
        cryptocurrency.$item.find(".price").text(cryptocurrency.price);
        cryptocurrency.volume_24h = fetchNewData(newData, 'total_volume', cryptocurrency.name);
        cryptocurrency.$item.find(".volume_24h").text(cryptocurrency.volume_24h);
        cryptocurrency.percent_change_24h = fetchNewData(newData, 'market_cap_change_percentage_24h', cryptocurrency.name);
        cryptocurrency.$item.find(".percent_change_24h").text(cryptocurrency.percent_change_24h);
    }
    cryptocurrencies.sort(descending);
    updateRanks(cryptocurrencies);
    reposition();
    console.log('Finished retrieving new data');

}
function getRandomScoreIncrease() {
    return getRandomBetween(50, 150);
}
function getRandomBetween(minimum, maximum) {
    return Math.floor(Math.random() * maximum) + minimum;
}
function resetBoard() {
    var $list = $("#cryptocurrencies");
    $list.find(".cryptocurrency").remove();
    if (timerId !== undefined) {
        clearInterval(timerId);
    }
    cryptocurrencies = [];
    for (let i = 0; i < 25; i++) {
        cryptocurrencies.push(
            {
                name: data[i].name,
                symbol: data[i].symbol,
                price: data[i].current_price,
                market_cap: data[i].market_cap,
                circulating_supply: Math.round(data[i].circulating_supply),
                volume_24h: data[i].total_volume,
                percent_change_24h: data[i].market_cap_change_percentage_24h,
            }
        )
    }

    for (var i = 0; i < cryptocurrencies.length; i++) {
        var $item = $(
            "<tr class='cryptocurrency'>" +
            "<th class='rank'>" + (i + 1) + "</th>" +
            "<td class='name'>" + cryptocurrencies[i].name + "</td>" +
            "<td class='symbol'>" + cryptocurrencies[i].symbol + "</td>" +
            "<td class='price'>" + cryptocurrencies[i].price + "</td>" +
            "<td class='market_cap'>" + cryptocurrencies[i].market_cap + "</td>" +
            "<td class='circulating_supply'>" + cryptocurrencies[i].circulating_supply + "</td>" +
            "<td class='volume_24h'>" + cryptocurrencies[i].volume_24h + "</td>" +
            "<td class='percent_change_24h'>" + cryptocurrencies[i].percent_change_24h + "</td>" +
            "</tr>"
        );

        cryptocurrencies[i].$item = $item;
        $list.append($item);
    }
    cryptocurrencies.sort(descending);
    updateRanks(cryptocurrencies);
    reposition();

    // fetch new data for the updateInterval
    timerId = setInterval("getNewData();", updateInterval);

}