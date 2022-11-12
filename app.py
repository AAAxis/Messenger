from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)



#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#    username="Rachinsky",
#    password="1111111@",
#    hostname="Rachinsky.mysql.pythonanywhere-services.com",
#    databasename="myappdb",)

#app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgresql@localhost:5433/flasksql'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'

db = SQLAlchemy(app)




@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    # Create aString
    def __repr__(self):
        return '<Name %r>' % self.name


if __name__=="__main__":
    app.run(debug=True)