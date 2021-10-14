// SIGNUP FORM JS
let formSignup = document.getElementById("formSignup");

let users = localStorage.getItem("user")
let usersList = [] //trống
if(users){
  usersList = JSON.parse(localStorage.getItem("user"))
}

formSignup.onsubmit = function (e) { // function báo lỗi
    e.preventDefault();

    setTextError("#emailError", "");
    setTextError("#passwordError", "");  //reset lỗi

    let email = formSignup.email.value;
    let password = formSignup.password.value;

    let validate = true;

    if (!email) {
        setTextError("#emailError", "Email is required");
        validate = false;
    }
    if (!password) {
        setTextError("#passwordError", "Password is required");
        validate = false;
    }
    if (password.length < 6) {
        setTextError("#passwordError", "Password length must be more than 6 characters");
        validate = false;
    }

    if (validate) {
        let user = {
            email: email,
            password: password,
        }
        usersList.push(user);
        localStorage.setItem("user", JSON.stringify(usersList));
    }

};

function setTextError(query, content) {
    document.querySelector(query).innerHTML = content;
}
