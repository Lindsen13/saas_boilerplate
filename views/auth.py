from flask import Blueprint, render_template, request, redirect, url_for, session

from model import check_username_exists, check_login_password, register_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user."""
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        register_user()
        return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET"])
def login():
    """Login a user."""
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("auth.home"))


@auth_bp.route("/check_username_exists", methods=["POST"])
def check_user_login():
    """Check if the username exists."""
    if check_username_exists():
        return "true"
    return "false"


@auth_bp.route("/check_login_password", methods=["POST"])
def check_user_password():
    """Check if the password is correct."""
    if check_login_password():
        return "true"
    return "false"


# Forgot Password
@auth_bp.route("/forgot_password", methods=["GET"])
def forgot_password():
    """Forgot password route."""
    return render_template("forgot-password.html")
