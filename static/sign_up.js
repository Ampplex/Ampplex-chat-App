class Redirect {
  redirectToSignUpPage() {
    // Redirecting to SignUp Page
    location.href = "http://192.168.0.5:5000/SignUp";
  }
  redirectToLoginPage() {
    // Redirecting to Login Page
    location.href = "http://192.168.0.5:5000/";
  }
}

class Display {
  showMessage(type, displayMsg) {
    let boldText;

    if (type == "success") {
      boldText = "Success!";
    } else {
      boldText = "Error!";
    }

    const msg = document.getElementById("message");
    let InnerHtml = `
                    <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                        <strong>${boldText}</strong> ${displayMsg}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
    `;
    msg.innerHTML = InnerHtml;
    setTimeout(() => {
      msg.InnerHtml = "";
    }, 20000);
  }
}

// const LoginBtnHandler = () => {};

const SignUpBtnHandler = (e) => {
  // Verifying both the passwords
  let display = new Display();
  if (password.value != confirm_password.value) {
    // alert("password and confirm password must be same");
    display.showMessage("danger", "password and confirm password must be same");
  } else if (password.value.length < 8 && confirm_password.value.length < 8) {
    display.showMessage(
      "danger",
      "password length must be more than 8 characters"
    );
  } else {
    // alert("success", "Signed-Up successfully!");
    display.showMessage("success", "Signed-Up successfully!");
  }
  e.preventDefault();
};

const AppBrand = document.getElementById("App-Brand");
const home_page = document.getElementById("home");
const password = document.getElementById("user_password");
const confirm_password = document.getElementById("confirm_user_password");
const SignUpBtn = document.getElementById("SignUp-Btn");
const progress_bar = document.getElementById("progress_bar");
const LoginBtn = document.getElementById("Login-Btn");

let redirect = new Redirect();

AppBrand.addEventListener("click", redirect.redirectToLoginPage);
home_page.addEventListener("click", redirect.redirectToLoginPage);
SignUpBtn.addEventListener("click", function () {
  progress_bar.innerHTML = `
          <div class="progress"
          style=" animation-name: ProgressAnimation; animation-duration: 9s; animation-iteration-count: infinite;">
        </div>
  `;
  SignUpBtnHandler();
});
