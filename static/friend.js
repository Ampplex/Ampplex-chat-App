const SendBtnHandler = (message) => {
  const unique_id = document.querySelector(".unique-id").id;

  // Retreiving chats
  let retrieved_msg = localStorage.getItem(unique_id);
  retrieved_msg = JSON.parse(retrieved_msg);

  if (retrieved_msg == null) {
    let Message_lst = [];
    Message_lst.push(message);
    localStorage.setItem(unique_id, JSON.stringify(Message_lst));
  } else {
    let Message_lst = retrieved_msg;
    Message_lst.push(message);
    localStorage.setItem(unique_id, JSON.stringify(Message_lst));
  }
};

const ProfileHandler = () => {
  location.href = "http://192.168.0.5:7777/MyProfile";
};

const homePageRedirecter = () => {
  location.href = "http://192.168.0.5:7777/chatroom";
};

const ShowChats = () => {
  const unique_id = document.querySelector(".unique-id").id;
  const userChatDiv = document.getElementById("user-chats"); // User Chats main div

  let chats_retreived = localStorage.getItem(unique_id);
  chats_retreived = JSON.parse(chats_retreived);
  if (chats_retreived != null) {
    let chats = "";
    chats_retreived.forEach(function (chat) {
      chats += `
                <div class="chats">
                  <p>${chat}</p>
                </div>
      `;
    });
    userChatDiv.innerHTML = chats;
  }
};

const message = document.getElementById("message");
const send_btn = document.getElementById("send-btn");
const my_profile = document.getElementById("MyProfile-Btn");
const home = document.getElementById("home");

send_btn.addEventListener("click", () => {
  SendBtnHandler(message.value);
});

my_profile.addEventListener("click", ProfileHandler);

home.addEventListener("click", homePageRedirecter);

ShowChats();
