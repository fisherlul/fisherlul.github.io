// Dùng cú pháp của JSON

// Hàm map 

// Tác dụng: tương tự như for, ưu điểm ngắn gọn, nó sẽ chạy từ đầu phần tử đến cuối cùng, không bỏ qua bất kì phần tử nào

var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
// for(let i = 0; i < arr.length; i++){
//     console.log(arr[i]);
// }
arr.map(function (index) {
    console.log(index);
});

// map là 1 hàm map(abc)
// for(let i = 0; i < arr.length; i++) {
//     if(arr[i] > 2){
//         console.log(arr[i]);
//     }
// }

console.log("---------------------");
//hàm filter có tác dụng lọc, về bản chất vẫn giống vòng for, nó sẽ lọc ra và trả về kết quả tương ứng với biểu thức điều kiện đã cho
// arr.filter(function(index){
//     if(index < 2) {
//         console.log(index)
//     }
// });
console.log(
    arr.filter(function (index) {
        return index > 2;
    })
);

// Arrow function: () => {}

// function phepCong(a, b) {
//     return a + b;
// }

//--------
// var phepCong = (a, b) => {
//     return a + b;
// }

var phepCong = (a, b) => a + b;
console.log(phepCong(1, 2));

var conText = () => {
    console.log("this is param")
}

conText();

//sử dụng arr with fn map

arr.map((index) => console.log(index));