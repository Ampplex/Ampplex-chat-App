class Login {
  redirectToSignUpPage() {
    // Redirecting to SignUp Page when user clicks on SignUp
    location.href = "http://127.0.0.1:1010/SignUp";
  }
}

let login = new Login();

const SignUpBtn = document.getElementById("SignUp_nav");

SignUpBtn.addEventListener("click", login.redirectToSignUpPage);
