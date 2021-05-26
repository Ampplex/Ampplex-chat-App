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
    // history.go(-1);
    location.href = "http://192.168.0.5:5000/chatroom";
  }
  redirectToEditProfile() {
    location.href = "http://192.168.0.5:5000/Edit_Profile";
  }
}

let redirect = new Redirect();

const home = document.getElementById("home");
const settings = document.getElementById("settings");
const edit_profile = document.getElementById("edit-profile");

home.addEventListener("click", () => {
  redirect.redirectToChatroom();
});

// When user clicks on edit profile then redirecting to edit profile page

edit_profile.addEventListener("click", () => {
  redirect.redirectToEditProfile();
});

// Settings wheel rotation
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
