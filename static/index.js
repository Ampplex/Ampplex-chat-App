class Redirect {
  redirectToSignUpPage() {
    // Redirecting to SignUp Page
    location.href = "http://127.0.0.1:1010/SignUp";
  }
  redirectToLoginPage() {
    // Redirecting to Login Page
    location.href = "http://127.0.0.1:1010/";
  }
}

let redirect = new Redirect();

const SignUpBtn = document.getElementById("SignUp_nav");
const AppBrand = document.getElementById("App-Brand");
const home_page = document.getElementById("home");
const loginBtn = document.getElementById("Login-Btn");

SignUpBtn.addEventListener("click", redirect.redirectToSignUpPage);
AppBrand.addEventListener("click", redirect.redirectToLoginPage);
home_page.addEventListener("click", redirect.redirectToLoginPage);
