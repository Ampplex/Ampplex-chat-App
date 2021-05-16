class Redirect {
  redirectToSignUpPage() {
    // Redirecting to SignUp Page
    location.href = "http://127.0.0.1:1010/SignUp";
  }
  redirectToLoginPage() {
    // Redirecting to Login Page
    location.href = "http://127.0.0.1:1010/";
  }

  redirectToUserProfile() {
    location.href = "http://127.0.0.1:1010/MyProfile";
  }
  redirectToFriendPage() {
    location.href = "http://127.0.0.1:1010/Friend";
  }
  redirectToChatroom() {
    location.href = "http://127.0.0.1:1010/chatroom";
  }
}

let redirect = new Redirect();

let home = document.getElementById("home");
let settings = document.getElementById("settings");

home.addEventListener("click", () => {
  redirect.redirectToChatroom();
});

settings.addEventListener("mouseover", () => {
  settings.setAttribute(
    "style",
    "position: absolute; left: 60rem; top: 8rem; top: 9rem; animation-name: rotateSetting; animation-duration: 1.5s; animation-iteration-count: 1;"
  );
});

settings.addEventListener("mouseleave", () => {
  settings.setAttribute(
    "style",
    "position: absolute; left: 60rem; top: 8rem; top: 9rem;"
  );
});
