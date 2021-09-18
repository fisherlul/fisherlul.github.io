let formSignup = document.getElementById("formSignup");

let userList = JSON.parse(localStorage.getItem("user"))

formSignup.onsubmit = function (e) {
    e.preventDefault();

    setTextError("#emailError", "");
    setTextError("#passwordError", "");  //reset lỗi

    let email = formSignup.email.value;
    let password = formSignup.password.value;

    localStorage.setItem("email", email);
    localStorage.setItem("password", password);

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
        userList.push(user);
        localStorage.setItem("user", JSON.stringify(userList));
    }

};

function setTextError(query, content) {
    document.querySelector(query).innerHTML = content;
}

function Redirect() {
    location.replace("wa/lesson6/btvn/main.html");
}
