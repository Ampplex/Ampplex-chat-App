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
    }, 5000);
  }
}

const SignUpBtnHandler = () => {
  // Verifying both the passwords
  let display = new Display();
  if (password.value != confirm_password.value) {
    display.showMessage("danger", "password and confirm password must be same");
  } else {
    display.showMessage("success", "Signed-Up successfully!");
  }
};

const AppBrand = document.getElementById("App-Brand");
const home_page = document.getElementById("home");
const password = document.getElementById("user_password");
const confirm_password = document.getElementById("confirm_user_password");
const SignUpBtn = document.getElementById("SignUp-Btn");

let redirect = new Redirect();

AppBrand.addEventListener("click", redirect.redirectToLoginPage);
home_page.addEventListener("click", redirect.redirectToLoginPage);
SignUpBtn.addEventListener("click", SignUpBtnHandler);
