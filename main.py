from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user_info.dp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Ampplex_UserAuthentication(db.Model):
    def __init__(self):
        self.sno = db.Column(db.Integer, primary_key=True)
        self.user_name = db.Column(db.String(200), nullable=False)
        self.user_email_id = db.Column(db.String(200), nullable=False)
        self.user_password = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.user_name} - {self.user_email_id} - {self.user_password}"


@app.route('/')
def User_Auth():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=1010)
