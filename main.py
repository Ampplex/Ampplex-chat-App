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
        return f"[{self.sno} , {self.user_name} , {self.user_email_id} , {self.user_password}]"


@app.route('/', methods=['GET', 'POST'])
def User_Auth():
    if request.method == "POST":
        email_id = request.form['user_email_id']
        password = request.form['user_password']
        speak(email_id+password)
        speak("Hello World")

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

            User_Info = Ampplex_UserAuthentication(
                user_name=name, user_email_id=email_id, user_password=password)
            db.session.add(User_Info)
            db.session.commit()

        Data = Ampplex_UserAuthentication.query.all()
        print(Data)

    return render_template('sign_up.html', InnerHtml=InnerHtml)


if __name__ == '__main__':
    app.run(debug=True, port=1010)
