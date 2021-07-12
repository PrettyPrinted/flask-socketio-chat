from flask import Flask 
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
	msg = msg.encode('latin-1').decode('utf-8')
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app)
