from flask import Blueprint, render_template, request, redirect, url_for, session

from model import checkloginusername, checkloginpassword, checkusername, register_user

auth_bp = Blueprint('auth', __name__)


# Register new user
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        register_user()
        return redirect(url_for("auth.login"))


# Check if email already exists in the registratiion page
@auth_bp.route("/checkusername", methods=["POST"])
def check():
    return checkusername()


# Everything Login (Routes to renderpage, check if username exist and
# also verifypassword through Jquery AJAX request)
@auth_bp.route("/login", methods=["GET"])
def login():
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("auth.home"))


@auth_bp.route("/checkloginusername", methods=["POST"])
def checkUserlogin():
    return checkloginusername()


@auth_bp.route("/checkloginpassword", methods=["POST"])
def checkUserpassword():
    return checkloginpassword()


# Forgot Password
@auth_bp.route("/forgot-password", methods=["GET"])
def forgotpassword():
    return render_template("forgot-password.html")
