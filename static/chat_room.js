class Redirect {
  redirectToSignUpPage() {
    // Redirecting to SignUp Page
    location.href = "http://192.168.0.5:7777/SignUp";
  }
  redirectToLoginPage() {
    // Redirecting to Login Page
    location.href = "http://192.168.0.5:7777/";
  }
  redirectToUserProfile() {
    location.href = "http://192.168.0.5:7777/MyProfile";
  }
  redirectToFriendPage() {
    location.href = "http://192.168.0.5:7777/Friend";
  }
  redirectToChatroom() {
    location.href = "http://192.168.0.5:7777/chatroom";
  }
}

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
