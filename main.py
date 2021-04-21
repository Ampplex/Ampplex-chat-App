from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pyttsx3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user_info.dp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def speak(audio):
    pyttsx3.speak(audio)


class Ampplex_UserAuthentication(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), nullable=False)
    user_email_id = db.Column(db.String(200), nullable=False)
    user_password = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.user_name} - {self.user_email_id} - {self.user_password}"


@app.route('/', methods=['GET', 'POST'])
def User_Auth():
    if request.method == "POST":
        email_id = request.form['user_email_id']
        password = request.form['user_password']
        speak(email_id+password)
        speak("Hello World")

    return render_template('index.html')


@ app.route('/SignUp', methods=["GET", "POST"])
def SignUp_Auth():

    if request.method == "POST":
        name = request.form['user_name']
        email_id = request.form['user_email_id']
        password = request.form['user_password']
        User_Info = Ampplex_UserAuthentication(
            user_name=name, user_email_id=email_id, user_password=password)
        db.session.add(User_Info)
        Data = Ampplex_UserAuthentication.query.all()
        print(Data)

    return render_template('sign_up.html')


if __name__ == '__main__':
    app.run(debug=True, port=1010)
