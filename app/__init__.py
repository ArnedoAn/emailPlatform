from flask import Flask
from app.views.send import send
from app.views.login import login
from app.views.register import register
from app.views.activate import activate
from app.views.reset import reset
from app.views.messages import messages
from app.controllers.dbController import getSenderParams

app = Flask(__name__)

params = getSenderParams('4nDr3z.uninorte')
if(params!=False):
    app.config['MAIL_USERNAME'] = str(params[0])
    app.config['MAIL_PASSWORD'] = str(params[1])
else:
    print("Error credenciales de correo")    

app.register_blueprint(send)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(activate)
app.register_blueprint(reset)
app.register_blueprint(messages)
 

@app.route("/")
def home():
    return "<h1>Welcome home</h1>"
