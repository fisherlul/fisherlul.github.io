let formSignup = document.getElementById("formSignup")

formSignup.onsubmit = function(e){
    e.preventDefault();

    let email = formSignup.email.value
    let password = formSignup.password.value
    let cfpassword = formSignup.cfpassword.value


    
}

let users = [
    {
        email: "a@a",
        password: "alo",
    }
];

console.log(users[1].email)

