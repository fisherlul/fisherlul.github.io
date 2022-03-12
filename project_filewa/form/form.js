let users = localStorage.getItem("user")
let usersList = []
if (users) {
    usersList = JSON.parse(localStorage.getItem("user"))
}
// SIGNIN FORM JS
let domSignin = document.querySelector("#formSignIn");

domSignin.onsubmit = function (e) {

    e.preventDefault();

    // let email = domSignin.email_signin.value;
    // let password = domSignin.password_signin.value;

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
    var email = document.getElementById('email_signin').value;
    var password = document.getElementById('password_signin').value;

    // signInWithEmailAndPassword(auth, email, password)
    //     .then((userCredential) => {
    //         // Signed in 
    //         const user = userCredential.user;

    //         const dt = new Date();
    //         update(ref(database, 'users/' + user.uid), {
    //             last_login: dt,
    //         })
            window.open("../main page/home.html", "_self")
    //     })
    //     .catch((error) => {
    //         const errorCode = error.code;
    //         const errorMessage = error.message;

    //         alert(errorMessage);
    //     });
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

    let username = formSignup.user.value;
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
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { doc, getDoc, setDoc, collection, addDoc} from "https://www.gstatic.com/firebasejs/9.6.8/firebase-firestore.js";
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
const db = getFirestore();

let getData = async () => {
    let ref = await doc(db, "user", "information")
    let data = await getDoc(ref)
    console.log(data);
}

getData()

signUp.addEventListener('click', async(e) => {
    if (container.classList.contains("right-panel-active")) {
        var email = document.getElementById('email_signup').value;
        var password = document.getElementById('password_signup').value;
        var username = document.getElementById('username').value;

        // createUserWithEmailAndPassword(auth, email, password)
        //     .then((userCredential) => {
        //         // Signed in 
        //         const user = userCredential.user;

        //         set(ref(database, 'users/' + user.uid), {
        //             username: username,
        //             email: email
        //         });
        //         sweetAlert("success", "Sign Up Successfully");
        //         window.open("../main page/home.html", "_self")
        //     })
        //     .catch((error) => {
        //         const errorCode = error.code;
        //         const errorMessage = error.message;

        //         alert(errorMessage);
        //         // ..
        //     });
        const docRef = await addDoc(collection(db, "user"), {
            name: username,
            email: email,
            password: password
        });
        console.log("Document written with ID: ", docRef.id);
    }
});

// login.addEventListener('click', (e) => {
    

// });
