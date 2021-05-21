class Redirect {
  redirectToSignUpPage() {
    // Redirecting to SignUp Page
    location.href = "http://192.168.0.5:5000/SignUp";
  }
  redirectToLoginPage() {
    // Redirecting to Login Page
    location.href = "http://192.168.0.5:5000/";
  }
  redirectToUserProfile() {
    location.href = "http://192.168.0.5:5000/MyProfile";
  }
  redirectToFriendPage() {
    location.href = "http://192.168.0.5:5000/Friend";
  }
  redirectToChatroom() {
    location.href = "http://192.168.0.5:5000/chatroom";
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
console.log("{{UserData}}");

let redirect = new Redirect();

const Profile = document.getElementById("MyProfile-Btn");
Profile.addEventListener("click", redirect.redirectToUserProfile);

// Adding event lisner to all the user and redirecting them to friend.html

const users = document.querySelector(".user");
for (let i = 0; i < users.children.length; i++) {
  users.children[i].addEventListener("click", () => {
    redirect.redirectToFriendPage();
  });
}
