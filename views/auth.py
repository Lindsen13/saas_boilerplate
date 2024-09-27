from typing import Any

from flask import Blueprint, redirect, render_template, request, session, url_for

from utils.auth import (
    check_login_password,
    check_username_exists,
    register_user,
    update_name_from_user,
    login_required,
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register() -> Any:
    """Register a new user."""
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        register_user()
        return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET"])
def login() -> Any:
    """Login a user."""
    if "username" not in session:
        return render_template("login.html")
    else:
        return redirect(url_for("base.home"))


@auth_bp.route("/check_username_exists", methods=["POST"])
def check_user_login() -> str:
    """Check if the username exists."""
    if check_username_exists():
        return "true"
    return "false"


@auth_bp.route("/check_login_password", methods=["POST"])
def check_user_password() -> str:
    """Check if the password is correct."""
    if check_login_password():
        return "true"
    return "false"


@auth_bp.route("/forgot_password", methods=["GET"])
def forgot_password() -> Any:
    """Forgot password route."""
    return render_template("forgot-password.html")


@auth_bp.route("/update_name", methods=["POST"])
@login_required
def update_name() -> Any:
    """Update name route."""
    if update_name_from_user(
        username=session.get("username"), new_name=request.args.get("name")
    ):
        return "true"
    return "false"
