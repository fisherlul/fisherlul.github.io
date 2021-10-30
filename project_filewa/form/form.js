let users = localStorage.getItem("user")
let usersList = []
if (users) {
    usersList = JSON.parse(localStorage.getItem("user"))
}
// SIGNIN FORM JS
let domSignin = document.querySelector("#formSignIn");

domSignin.onsubmit = function (e) {

    e.preventDefault();

    let email = domSignin.email_signin.value;
    let password = domSignin.password_signin.value;

    for (let i = 0; i < usersList.length; i++) {
        if (usersList[i].email == email) {
            if (usersList[i].password == password) {
                window.open("../main page/home.html", "_self")
            } else {
                console.log("Wrong Password!")
            }
            break
        } else {
            sweetAlert("error", "email does not exist")
        }
    }
};

// FORM EFFECTS
const signInBtn = document.getElementById("signIn");
        const signUpBtn = document.getElementById("signUp");
        const fistForm = document.getElementById("formSignUp");
        const secondForm = document.getElementById("formSignIn");
        const container = document.querySelector(".container");

        signInBtn.addEventListener("click", () => {
            container.classList.remove("right-panel-active");
        });

        signUpBtn.addEventListener("click", () => {
            container.classList.add("right-panel-active");
        });

        fistForm.addEventListener("submit", (e) => e.preventDefault());
        secondForm.addEventListener("submit", (e) => e.preventDefault());
   
// SIGNUP FORM 
let formSignup = document.querySelector("#formSignUp");

formSignup.onsubmit = function (e) { 

    setTextError("#emailError", "");
    setTextError("#passwordError", "");  

    let username = formSignUp.user.value;
    let email = formSignup.email_signup.value;
    let password = formSignup.password_signup.value;

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
            username: username,
            email: email,
            password: password,
        }
        usersList.push(user);
        localStorage.setItem("user", JSON.stringify(usersList));
        sweetAlert("success", "Sign Up Successfully");
        window.open("../main page/home.html", "_self")
    }

};

function setTextError(query, content) {
    document.querySelector(query).innerHTML = content;
}

function sweetAlert(icon, message) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })
    
    Toast.fire({
        icon: icon,
        title: message,
    })
    
}