// SIGNIN FORM JS
let domSignin = document.getElementsByClassName("container--signin");

let users = localStorage.getItem("user")
let usersList = []
if (users) {
    usersList = JSON.parse(localStorage.getItem("user"))
}

domSignin.onsubmit = function (e) {
    let email = domSignin.email.value;
    let password = domSignin.password.value;

    for (let i = 0; i < usersList.length; i++) {
        if (usersList[i].email == email) {
            if (usersList[i].password == password) {
                window.open("./home.html", "_self")
            } else {
                console.log("Wrong Password!")
            }
            break
        } else {
            sweetAlert("error", "email does not exist")
        }
    }
};

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

// FORM EFFECTS
const signInBtn = document.getElementById("signIn");
        const signUpBtn = document.getElementById("signUp");
        const fistForm = document.getElementById("form1");
        const secondForm = document.getElementById("form2");
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
let formSignup = document.getElementsByClassName("container--signup");

formSignup.onsubmit = function (e) { 

    setTextError("#emailError", "");
    setTextError("#passwordError", "");  
    setTextError("#cfPasswordError", "");

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