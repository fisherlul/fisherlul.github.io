localStorage.clear();

// var email = document.getElementById("email");
// var password = document.getElementById("password");
// var cfpassword = document.getElementById("cfpassword");

function Submit() {
    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var cfpassword = document.getElementById("cfpassword");

    localStorage.setItem("email", email.value);
    localStorage.setItem("password", password.value);
    localStorage.setItem("cfpassword", cfpassword.value)
}