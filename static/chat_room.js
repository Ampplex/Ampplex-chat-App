// import { error, require } from "util";

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

const Profile = document.getElementById("MyProfile-Btn");

Profile.addEventListener("click", redirect.redirectToUserProfile);
