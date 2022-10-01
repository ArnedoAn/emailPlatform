from flask import Flask
from views.send import send
from views.login import login
from views.register import register
from views.activate import activate
# from views.change import change
# from views.recovery import recovery
# from views.messages import messages

app = Flask(__name__)
app.app_context()

app.register_blueprint(send)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(activate)
# app.register_blueprint(change)
# app.register_blueprint(recovery)
# app.register_blueprint(messages)


@app.route("/")
def home():
    return "<h1>Welcome home</h1>"

