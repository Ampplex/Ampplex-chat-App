/*
Copyright (c) Ampplex Technologies Pvt.Ltd. All rights reserved

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

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
          style=" animation-name: ProgressAnimation; animation-duration: 8s; animation-iteration-count: 1;">
        </div>
  `;
  SignUpBtnHandler();
});
