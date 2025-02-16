let formSignup = document.getElementById("formSignup");

formSignup.onsubmit = function(e) {
    e.preventDefault();
    
    let email = document.getElementById("email");
    let password = document.getElementById("password");
    let cfpassword = document.getElementById("cfpassword");

    localStorage.setItem("email", email.value);
    localStorage.setItem("password", password.value);
    localStorage.setItem("cfpassword", cfpassword.value);

    if(password != cfpassword){
        alert("Password not matched.")
    }
}