
from flask import Flask, render_template


app = Flask(__name__)


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{Rachinsky}:{111111}@{rachinsky.mysql.pythonanywhere-services.com}/{myappdb}".format()
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgresql@localhost:5433/flasksql'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(120), default='image.jpg')
    password = db.Column(db.String(100), nullable=False)
    isActive = db.Column(db.Boolean, default=True)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
