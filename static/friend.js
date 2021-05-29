const SendBtnHandler = (message) => {
  const unique_id = document.querySelector(".unique-id").id;
  let retrieved_msg = localStorage.getItem(unique_id);
  retrieved_msg = JSON.parse(retrieved_msg);
  console.log("msg: ", retrieved_msg);
  if (retrieved_msg == null) {
    let Message_lst = [];
    Message_lst.push(message);
    localStorage.setItem(unique_id, JSON.stringify(Message_lst));
    console.log(Message_lst);
  } else {
    let Message_lst = retrieved_msg;
    Message_lst.push(message);
    localStorage.setItem(unique_id, JSON.stringify(Message_lst));
    console.log(Message_lst);
  }
};

const message = document.getElementById("message");
const send_btn = document.getElementById("send-btn");

send_btn.addEventListener("click", () => {
  SendBtnHandler(message.value);
});
