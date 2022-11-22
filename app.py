from flask import Flask, render_template, url_for, redirect, session, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
#secret key etc...
...
@socketio.on('message')
def handle_msg(msg):
    socketio.send('Syncing...')

if __name__ == '__main__':
    socketio.run(app)
