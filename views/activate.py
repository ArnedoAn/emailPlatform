from flask import Blueprint, request


activate = Blueprint('activate', __name__, template_folder='templates')

@activate.get("/activate")
def activateUser():
    data = {}
    data["email"] = request.args.get('email')
    data["cod"] = request.args.get('cod')
    