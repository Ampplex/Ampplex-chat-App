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


from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import pyttsx3
import requests
import json
import socket
from datetime import datetime, timedelta
from random import randint
from cryptography.fernet import Fernet


app = Flask(__name__)
app.secret_key = "dkfgkodfmnklxk jknfjfksnrfro34h8793P:P}{%$$%^.;.,;.<<>>:L::>PL>::{:}{{}__+_+_::>///*-*-;[;[]sfrgdfgth::_+()()*(#$%^&)]},;',.l;``opo`pkpo`jp`p;"
app.permanent_session_lifetime = timedelta(days=30)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user_info.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
key = Fernet.generate_key()
f = Fernet(key)


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    pyttsx3.speak(audio)
    engine.say(audio)
    engine.runAndWait()


def getHostName():
    return socket.gethostname()


def getDateTime():
    return datetime.today().date()


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
    dateUserJoined = db.Column(db.String(100), nullable=False)
    uniqueId = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} , {self.user_name} , {self.user_email_id} , {self.country_name} , {self.user_password}, {self.host_name}, {self.dateUserJoined}, {self.uniqueId}"


def splitUserData(USER_DATA):
    # FoundSno = 0  # Storing the Sno of the user to use the data in the chat app after login
    for i in range(len(USER_DATA)):
        USER_DATA[i] = str(USER_DATA[i]).split(',')
    return USER_DATA


def Logout_User():
    session.clear()
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def User_Auth():
    if "user" in session:
        return redirect('/chatroom')

    USER_DATA = Ampplex_UserAuthentication.query.all()
    splitUserData(USER_DATA)

    if request.method == "POST":
        # Retreving email and password
        email_id = request.form['user_email_id'].strip()
        password = request.form['user_password'].strip()

        # Scanning the database to ensure that the email-Id and Password are correct
        flag_EmailFound = False
        if email_id != "" and password != "":
            for i in range(len(USER_DATA)):
                email_id_retrieved = USER_DATA[i][2]
                password_retrieved = USER_DATA[i][4]
                if email_id_retrieved.strip() == email_id:
                    flag_EmailFound = True
                    if password_retrieved.strip() == password:
                        session.permanent = True
                        session["user"] = USER_DATA[i]
                        speak("Successfully Logined")
                        print("[NEW USER SUCCESSFULLY LOGINED]")
                        try:
                            return redirect('/chatroom')
                        except Exception as e:
                            speak(
                                'Some error occured while trying to redirect to chatroom')
                            print(e)
                    else:
                        speak("Error: password or email id must be valid and correct")

            if flag_EmailFound == False:
                speak("Please sign up if you don't have an Ampplex Account")
        elif email_id == "" and password == "":
            speak("Please enter the email-Id and password to login")

    return render_template('index.html')


@app.route('/SignUp', methods=["GET", "POST"])
def SignUp_Auth():
    USER_DATA = Ampplex_UserAuthentication().query.all()
    splitUserData(USER_DATA)
    uniqueId = randint(len(USER_DATA)*10, len(USER_DATA)*1000)
    if request.method == "POST":
        name = request.form['user_name']
        email_id = request.form['user_email_id']
        password = request.form['user_password']
        confirm_password = request.form['confirm_user_password']

        country_name = Fetch_CountryName()

        host_name = getHostName()

        encrypted_hostname = f.encrypt(host_name.encode())
        print("HELLO WORLD ENCRYPTED", encrypted_hostname)

        if name != "" and email_id != "" and password != "":
            if email_id in USER_DATA:
                speak(f'{email_id} already exist please use a different Email-ID')
                return render_template('sign_up.html')
            elif len(password) >= 8:
                User_Info = Ampplex_UserAuthentication(
                    user_name=name, user_email_id=email_id, user_password=password, country_name=country_name, host_name=encrypted_hostname, dateUserJoined=getDateTime(), uniqueId=uniqueId)
                db.session.add(User_Info)
                db.session.commit()
                print("[NEW USER SUCCESSFULLY SIGNED-UP]")
                return redirect('/')

    return render_template('sign_up.html')


@app.route('/chatroom')
def ChatRoom():
    # Removing the user logined from the recommendation to give proper recommendation
    USER_DATA = Ampplex_UserAuthentication().query.all()

    if len(USER_DATA) > 0:
        if "user" in session:
            user = session["user"]
            Index = user[0]
            USER_DATA.remove(USER_DATA[int(Index)-1])

            return render_template('chatroom.html', UserData=USER_DATA)
    else:
        return redirect('/')


@app.route('/MyProfile', methods=['GET', 'POST'])
def MyProfile():
    if "user" in session:
        user = session["user"]
        if request.method == 'POST':
            if request.form.get('logout_user'):
                Logout_User()

        return render_template('user_profile.html', userInfo=user)
    else:
        return redirect('/')


@app.route('/Friend/<string:hostname>')
def Friend(hostname):
    decrypted_hostname = f.decrypt(hostname).decode()
    print(decrypted_hostname)
    return render_template('friend.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
