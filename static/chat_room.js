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

function speak(audio) {
  let speech = new SpeechSynthesisUtterance();
  speech.lang = "en-US";
  speech.text = audio;
  speech.volume = 1;
  speech.rate = 1;
  speech.pitch = 1;

  window.speechSynthesis.speak(speech);
}

speak("Welcome to Ampplex Chat Room");
let redirect = new Redirect();

const Profile = document.getElementById("MyProfile-Btn");

Profile.addEventListener("click", redirect.redirectToUserProfile);
