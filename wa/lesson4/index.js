// Bài 1: viết 1 hàm truyền vào 1 số nguyên dương n. Viết hàm tính n giai thừa (n!). 

function findFactorial() {
    var n = prompt("Nhập số để tính giai thừa: ");
    var factorial = 1
    for (i = 1; i <= n; i++) {
        factorial + factorial * n;
    }
    console.log(factorial);
}

// Bài 2: Cho 1 chuỗi số, hãy viết loop có tác dụng sao chép chuỗi số lên 10 lần, ngăn cách nhau bởi ký tự "-". 

function loopTheStringTenTimes() {
    var str = prompt("Nhập vào 1 chuỗi kí tự bất kì");
    var loopResult = "";
    for (var i = 0; i < 10; i++) {
        loopResult = loopResult + `${str}-`;
    }
    console.log(loopResult);
}

// Bài 3: in ra các số từ 0 - 50 chia hết cho 2, 3, 5

console.log("Chia hết cho 2")
for (let i = 0; i <= 50; i++) {
    if (i % 2 == 0) {
        console.log(i)
    }
}

console.log("Chia hết cho 3")
for (let i = 0; i <= 50; i++) {
    if (i % 3 == 0) {
        console.log(i)
    }
}

console.log("Chia hết cho 4")
for (let i = 0; i <= 50; i++) {
    if (i % 4 == 0) {
        console.log(i)
    }
}


// Bài 6: viết 1 hàm truyền vào số và in ra thứ, các số tương ứng với số như sau

var n = prompt("Nhập một số: ");
function daySet() {
    if (n <= 7) {
        console.log("Hôm nay là thứ " + n )
    }
    if (n == 0) {
        console.log("Hôm nay là Chủ Nhật" )
    }
    else{
        console.log("Số nhập vào không hợp lệ")
    }
}
daySet(n)