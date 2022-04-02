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

// FIREBASE FORM

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
const auth = getAuth();
const db = getFirestore();

// SIGNUP FORM 
let formSignup = document.querySelector("#formSignUp");

formSignIn.onsubmit = async function (e) {

    let email_signin = document.getElementById("email_signin");
    let password_signin = document.getElementById("password_signin");

    e.preventDefault();

    signInWithEmailAndPassword(auth, email_signin.value, password_signin.value)
        .then((userCredential) => {
            alert("Logged in!")
            setTimeout(() => {
                alert("Redirecting...")
            },
            1 * 1000)
            setTimeout(
                () => {
                    alert("Redirecting...")
                    window.open("../main page/home.html", "_self")
                },
                3 * 1000
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

formSignup.onsubmit = async function (e) {
    e.preventDefault();

    setTextError("#emailError", "");
    setTextError("#passwordError", "");

    let username = formSignup.username.value;
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
        createUserWithEmailAndPassword(auth, email_signup, password_signup)
            .then((userCredential) => {
                Swal.fire({
                    title: 'Signed up sucessfully!',
                    icon: 'success',
                    confirmButtonText: 'Cool'
                  })
                setTimeout(
                    () => {
                        window.open("../main page/home.html", "_self")
                    },
                    3 * 1000
                );
            })
            .catch((error) => {
                console.log(error);
            });
        let user = {
            username: username,
            email: email_signup,
            password: password_signup,
        }
        localStorage.setItem('user', JSON.stringify(user));
    }
}

// formSignup.addEventListener('click', (e) => {
//     e.preventDefault();
    
//     let userfb = {
//         username: username,
//         email: email_signup,
//         password: password_signup,
//     }
//     .then(() => {
//         let ref = await collection(db, "user");
//         await addDoc(ref, userfb).then((result) => {
//             console.log('Succeed!')
//         }).catch((err) => {
//             console.log(err);
//         });
//     })
// })