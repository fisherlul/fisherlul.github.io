// Array - mảng

let array = [1, 2, 3, "string", "number", [1, 2, 3]]

console.log(array[0])
console.log(array,length)
console.log(array[5][1])

// for loop

for(let i = 0 ; i < array.length; i=i+1 ){
    console.log(array[i]);
}

// object - đối tượng

let object = {
    name: "Brad" ,
    age:"ur dad's age" ,

}
console.log(object.name)
let obPerson = {
    name: ["Huy", "Kev", "Josh", "Trung"]
}

console.log(obPerson.name)