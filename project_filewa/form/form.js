let users = localStorage.getItem("user")
let usersList = []
if (users) {
    usersList = JSON.parse(localStorage.getItem("user"))
}
// SIGNIN FORM JS
// 

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
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-analytics.js";
import { getAuth, onAuthStateChanged, signInWithPopup, signInWithEmailAndPassword, createUserWithEmailAndPassword, GoogleAuthProvider, GithubAuthProvider } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { doc, getDoc, setDoc, collection, addDoc, getFirestore } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-firestore.js";
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyAlMnXunsWZejvuuK4UJVI8UOALFVjMlyI",
    authDomain: "daily-bugle-d9265.firebaseapp.com",
    databaseURL: "https://daily-bugle-d9265-default-rtdb.firebaseio.com",
    projectId: "daily-bugle-d9265",
    storageBucket: "daily-bugle-d9265.appspot.com",
    messagingSenderId: "157991862579",
    appId: "1:157991862579:web:055a343ae639b7e6913e46",
    measurementId: "G-S9EHZ88WZQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth()
const db = getFirestore();

// SIGNUP FORM 
let formSignup = document.querySelector("#formSignUp");

formSignup.onsubmit = async function (e) {
    e.preventDefault();
    setTextError("#emailError", "");
    setTextError("#passwordError", "");

    let username = formSignup.user.value;
    let email_signup = formSignup.email_signup.value;
    let password_signup = formSignup.password_signup.value;

    let validate = true;

    if (!email_signup) {
        setTextError("#emailError", "Email is required");
        validate = false;
    }
    if (!password_signup) {
        setTextError("#passwordError", "Password is required");
        validate = false;
    }
    if (password_signup.length < 6) {
        setTextError("#passwordError", "Password length must be more than 6 characters");
        validate = false;
    }

    if (validate) {
        let user = {
            username: username,
            email: email_signup,
            password: password_signup,
        }
        let ref = await collection(db, "user");
        await addDoc(ref, user).then((result) => {
            alert("Succeed!")
            window.open("../main page/home.html", "_self")
        }).catch((err) => {
            console.log(err);
        });
        createUserWithEmailAndPassword(auth, email_signup, password_signup)
            .then((userCredential) => {
                alert("User created!")
            })
            .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;

                alert(errorMessage)
            });
    }

};
formSignIn.onsubmit = async function (e) {

    e.preventDefault();

    signInWithEmailAndPassword(auth, email_signin, password_signin)
        .then((userCredential) => {
            alert("Logged in!")
            setTimeout(
                () => {
                    alert("Succeed!")
                    window.open("../main page/home.html", "_self")
                },
                2 * 1000
            );
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.log("Error: " + errorMessage);
        });

}
// AUTHENTICATION
let gg_provider = new GoogleAuthProvider();
let gh_provider = new GithubAuthProvider();

document.getElementById("login-google").addEventListener("click", loginGoogle)
document.getElementById("login-github").addEventListener("click", loginGithub)

function loginGoogle() {
    signInWithPopup(auth, gg_provider)
        .then(result => {
            console.log(result.user);
            setTimeout(
                () => {
                    alert("Succeed!")
                    window.open("../main page/home.html", "_self")
                },
                2 * 1000
            );
        }).catch(err => {
            console.log(err);
        })
}

function loginGithub() {
    console.log('login');
    signInWithPopup(auth, gh_provider)
        .then(result => {
            console.log(result.user);
            setTimeout(
                () => {
                    alert("Succeed!")
                    window.open("../main page/home.html", "_self")
                },
                2 * 1000
            );
        }).catch(err => {
            console.log(err);
        })
}

export {loginGoogle, loginGithub};

onAuthStateChanged(auth, (user) => {
    if (user) {
      console.log("User is logged in");
      setTimeout(
        () => {
            alert("Succeed!")
            window.open("../main page/home.html", "_self")
        },
        2 * 1000
      );
    } else {
      console.log("Error");
    }
  });