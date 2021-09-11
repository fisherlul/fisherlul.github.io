let formSignup = document.getElementsByClassName("container__form container--signup")

formSignup.onsubmit = function() {
    e.preventDefault();
    
    let user = formSignup.user.value
    let email_signup = formSignup.email_signup.value
    let password_signup = formSignup.password_signup.value
}

// let users = [
//     {
//         email_signup: "a@a",
//         password_signup: "1"
//     },
//     {
//         email_signup: "b@a",
//         password_signup: "1"
//     },
//     {
//         email_signup: "c@a",
//         password_signup: "1"
//     },
//     {
//         email_signup: "d@a",
//         password_signup: "1"
//     },
//     {
//         email_signup: "e@a",
//         password_signup: "1"
//     },
// ]

