// Bài 1:

let student = (name, age, address) => {
    info = {
        name: "Hùng",
        age: 16,
        address: "Lĩnh Nam"
    }
    console.log('thông tin :', info);
}
student()


// Bài 2:

var smartPhones = [
    {
        name: 'iphone',
        price: 649
    },
    {
        name: 'Galaxy S6',
        price: 576
    },
    {
        name: 'Galaxy Note 5',
        price: 489
    }
]
smartPhones.map(function sm(a) {
    console.log(a.price);
})

// Bài 3

// function foo(x,y,z) {
// 	console.log( x, y, z );
// }

var foo = (x, y, z) => console.log(x, y, z)

// function foo() {
//     alert("Hello")
// }

var foo = () => alert("Hello")

// function foo(a, b) {
//     let m = a + b * 100
//     return m
// }

var foo = (a, b) => {
    let m = a + b * 100
    return m
}

// BTVN BUỔI 4 => ARROW FUNCTION

// Bài 1: viết 1 hàm truyền vào 1 số nguyên dương n. Viết hàm tính n giai thừa (n!). 

// function factorial(n) {
// let n = 8   // số ban đầu
// let result = 0   // biến lưu kết quả
// for (let i = 1; i <= n; i++) {
//     result = result * i
//     /* 1*1
//        1*1*2
//        1*1*2*3
//        .....  */
// }
// console.log(result);
// }

let factorial = (n) => {
    let n = 8   // số ban đầu
    let result = 0   // biến lưu kết quả
    for (let i = 1; i <= n; i++) {
        result = result * i
        /* 1*1
           1*1*2
           1*1*2*3
           .....  */
    }
    console.log(result);
}

// Bài 2: Cho 1 chuỗi số, hãy viết loop có tác dụng sao chép chuỗi số lên 10 lần, ngăn cách nhau bởi ký tự "-". 

// function loopTheStringTenTimes() {
//     var str = prompt("Nhập vào 1 chuỗi kí tự bất kì");
//     var loopResult = "";
//     for (var i = 0; i < 10; i++) {
//         loopResult = loopResult + `${str}-`;
//     }
//     console.log(loopResult);
// }

let loopTheStringTenTimes = () => {
    var str = prompt("Nhập vào 1 chuỗi kí tự bất kì");
    var loopResult = "";
    for (var i = 0; i < 10; i++) {
        loopResult = loopResult + `${str}-`;
    }
    console.log(loopResult);
}

// Bài 3: in ra các số từ 0 - 50 chia hết cho 2, 3, 5

// function chiaHet() {
// for (let i = 0; i <= 50; i++) {
//     if (i % 2 == 0) {
//         console.log(i)
//     }
// }


// for (let i = 0; i <= 50; i++) {
//     if (i % 3 == 0) {
//         console.log(i)
//     }
// }


// for (let i = 0; i <= 50; i++) {
//     if (i % 4 == 0) {
//         console.log(i)
//     }
// }
// }

let chiaHet = () => {
    for (let i = 0; i <= 50; i++) {
        if (i % 2 == 0) {
            console.log(i)
        }
    }


    for (let i = 0; i <= 50; i++) {
        if (i % 3 == 0) {
            console.log(i)
        }
    }


    for (let i = 0; i <= 50; i++) {
        if (i % 4 == 0) {
            console.log(i)
        }
    }
}


// Bài 6: viết 1 hàm truyền vào số và in ra thứ, các số tương ứng với số như sau

// var n = prompt("Nhập một số: ");
// function daySet() {
// if (n <= 7) {
//     console.log("Hôm nay là thứ " + n)
// }
// else if (n == 0) {
//     console.log("Hôm nay là Chủ Nhật")
// }
// else {
//     console.log("Số nhập vào không hợp lệ")
// }
// }
// daySet(n)

let daySet = () => {
    if (n <= 7) {
        console.log("Hôm nay là thứ " + n)
    }
    else if (n == 0) {
        console.log("Hôm nay là Chủ Nhật")
    }
    else {
        console.log("Số nhập vào không hợp lệ")
    }
}


