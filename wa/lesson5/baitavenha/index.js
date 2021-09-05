// Bài 1: Tạo 3 biến số và hiển thị bằng console & alert 

let firstName = "Nguyễn";
let surName = "Huy";
let lastName = "Hùng";
console.log(firstName + " " + surName + " " + lastName)
alert(firstName + " " + surName + " " + lastName)

// Bài 2: tính số dư phép chia một số bất kì

var n1 = prompt("Nhập số bị chia: ");
var n2 = prompt("Nhập số chia: ");
if (n1>n2){
    alert(n1 % n2);
    console.log(n1 % n2)
}else{
    alert("Kết quả là phân số, không có phần dư")
}

// Bài 3: Tính độ dài một string

var str = prompt("Nhập một chuỗi: ");
console.log("Độ dài chuỗi là: " + str.length);
alert("Độ dài chuỗi là: " + str.length)