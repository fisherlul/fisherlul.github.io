let array = [
    {
        name: "iphone 11",
        price: 10000
    },
    {
        name: "iphone 12",
        price: 6000
    }, {
        name: "iphone 13",
        price: 7000
    },
];
// 1. output: 1 mảng mới, giá giảm 25%
// 2. output: 1 mảng mới có các sản phẩm giá lớn hơn 6500

// arr.filter(function discount(a) {
//     if (price > 6500) {
//         console.log(price);
//     }
// })

// CHỮA BÀI

let sale = (discount) => {
    let a = arr.map((e) => {
        let rObj = {
            name: e.name,
            price: e.price * 0.75
        };
        return rObj;
    });
    console.log(a);
};
sale(0.25)


let b2 = arr.filter((e) => {
    return e.price > 6500
})
console.log(b2);