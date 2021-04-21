class Redirect {
  redirectToSignUpPage() {
    // Redirecting to SignUp Page when user clicks on SignUp
    location.href = "http://127.0.0.1:1010/SignUp";
  }
  redirectToLoginPage() {
    location.href = "http://127.0.0.1:1010/";
  }
}

let redirect = new Redirect();

const SignUpBtn = document.getElementById("SignUp_nav");

SignUpBtn.addEventListener("click", redirect.redirectToSignUpPage);
