from flask import Flask, render_template
from flask_socketio import SocketIO, emit, disconnect
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
#bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/info')
def info():
    # TODO: add your info.html call. 
    # A sample info.html file is already included. Please check info.html file and add your information
    # in that page as well.

if __name__ == '__main__':
    # Run HTTP and HTTPS servers in parallel using threading
    socketio.run(app, host='127.0.0.1', port=3009)
