"""
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
"""


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pyttsx3
import requests
import json
import socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user_info.dp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def speak(audio):
    pyttsx3.speak(audio)


def HostName():
    return socket.gethostname()


def Fetch_CountryName():
    # Fetching Country Name using user's ip address

    resp = requests.get('http://ip-api.com/json')
    return resp.json()['country']


class Ampplex_UserAuthentication(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), nullable=False)
    user_email_id = db.Column(db.String(200), nullable=False)
    user_password = db.Column(db.String(200), nullable=False)
    country_name = db.Column(db.String(300), nullable=False)
    host_name = db.Column(db.String(300), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} , {self.user_name} , {self.user_email_id} , {self.country_name} , {self.user_password}, {self.host_name}"


@app.route('/', methods=['GET', 'POST'])
def User_Auth():

    if request.method == "POST":
        email_id = request.form['user_email_id'].strip()
        password = request.form['user_password'].strip()
        USER_DATA = Ampplex_UserAuthentication.query.all()

        # Scaning the data base to ensure that the email-Id and Pass
        if email_id != "" and password != "":
            for i in range(len(USER_DATA)):
                email_id_retrieved = str(USER_DATA[i]).split(',')[2]
                password_retrieved = str(USER_DATA[i]).split(',')[4]
                flag_EmailFound = False
                if email_id_retrieved.strip() == email_id:
                    flag_EmailFound = True
                    if password_retrieved.strip() == password:
                        speak("Successfully Logined")
                        print("[NEW USER SUCCESSFULLY LOGINED]")
                        return redirect('/chatroom')
                    else:
                        speak("Error: password or email id must be valid and correct")

            if flag_EmailFound == False:
                speak("Please sign up if you don't have an Ampplex Account")
        elif email_id == "" and password == "":
            speak("Please enter the email-Id and password to login")

    return render_template('index.html')


def Display(type_msg, displayMsg):
    # boldText
    if type_msg == "success":
        boldText = "Success!"
    elif type_msg == "danger":
        boldText = "Error!"
    else:
        raise ValueError("Value of type_msg must be success or danger")

    InnerHtml = f"""
                                     <div class="alert alert-{type_msg} alert-dismissible fade show" role="alert">
                                        <strong>{boldText}</strong> {displayMsg}
                                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                    </div>
                """
    return InnerHtml


@app.route('/SignUp', methods=["GET", "POST"])
def SignUp_Auth():
    InnerHtml = ""
    if request.method == "POST":
        name = request.form['user_name']
        email_id = request.form['user_email_id']
        password = request.form['user_password']
        confirm_password = request.form['confirm_user_password']
        country_name = Fetch_CountryName()
        host_name = HostName()

        if name != "" and email_id != "" and password != "":

            if password != confirm_password:
                type_msg = "danger"
                displayMsg = "password and confirm password must be same"
                InnerHtml = Display(type_msg, displayMsg)

            elif len(password) < 8 and len(confirm_password) < 8:
                type_msg = "danger"
                displayMsg = "password length must be atleast 8 characters"

                InnerHtml = Display(type_msg, displayMsg)

            elif len(password) >= 8 and len(confirm_password) >= 8 and password == confirm_password:
                type_msg = "success"
                displayMsg = "password length must be atleast 8 characters"

                InnerHtml = Display(type_msg, displayMsg)
            if len(password) >= 8:
                User_Info = Ampplex_UserAuthentication(
                    user_name=name, user_email_id=email_id, user_password=password, country_name=country_name, host_name=host_name)
                db.session.add(User_Info)
                db.session.commit()

        Data = Ampplex_UserAuthentication.query.all()
        print(Data)

    return render_template('sign_up.html', InnerHtml=InnerHtml)


@app.route('/chatroom')
def ChatRoom():
    return render_template('chatroom.html')


if __name__ == '__main__':
    app.run(debug=True, port=1010)
