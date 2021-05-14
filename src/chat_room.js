// import { require } from "util";

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
}
// Connecting to user_info db
const sqlite3 = require("sqlite3").verbose();

let db = new sqlite3.Database("./user_info.db", (err) => {
  if (err) {
    console.log(err.message);
  }
  console.log("Connected to the user_info.db");

  db.all([], (err, rows) => {
    if (err) {
      console.log("Error occured!");
    }
    rows.forEach((row) => {
      console.log(row.user_name);
    });

    db.close((err) => {
      if (err) {
        console.log(err.message);
      }
    });

    console.log("Connection to db closed");
  });
});

let user_sno = document.querySelector(".user_sno").id;
console.log(`User sno is ${user_sno}`);

let redirect = new Redirect();

const Profile = document.getElementById("MyProfile-Btn");

Profile.addEventListener("click", redirect.redirectToUserProfile);
