from flask import Blueprint, request, render_template, session, redirect, flash, url_for
from app.controllers.pwdController import validatePwd

logout = Blueprint('login',__name__, template_folder='templates')

@logout.get('/logout')
def logout_user():
    session.clear()
    flash('Sesión cerrada!','info')
    return redirect(url_for("login.loginForm"))  