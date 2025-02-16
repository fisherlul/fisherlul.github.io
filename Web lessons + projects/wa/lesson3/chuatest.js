// bài 1

function findEven(number) {
    if (number < 4 && number < 20) {
        for (let i = 0; i < number; i++) {
            if (i % 2 == 0) {
                console.log(i);
            }
        }
    } else {
        console.log("số bạn nhập không hợp lệ")
    }
}

//bài 2
let doma = document.getElementById("a")

doma.addEventListener("mouseover", () => {
    doma.style.background = "yellow"
})
doma.addEventListener("mouseout", () => {
    doma.style.background = "red"
})

//bài 3
for (let i = 1; i < 6; i++) {
    let r = ""
    for (let j = 0; j < i; j++) {
        r += "1"
    }
    console.log(r)
}
//bài 4
let domb = document.querySelector("#b")
function renderTime() {
    let thoigian = new Date()

    let gio = thoigian.getHours()
    let phut = thoigian.getMinutes()
    let giay = thoigian.getSeconds()

    domb.innerHTML = gio + ":" + phut + ":" + giay
}

setInterval(renderTime, 1000)