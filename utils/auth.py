import json
from datetime import datetime, timezone
from functools import wraps

from bson import json_util
from flask import redirect, request, session, url_for

from utils.database import db
from utils.hashpass import hash_value
from utils.mail import sendmail


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function


def check_username_exists() -> bool:
    """Check if the username exists, return True if it does, False otherwise."""
    username = request.form["username"]
    check = db.users.find_one({"username": username})
    if check:
        return True
    else:
        return False


def check_login_password() -> bool:
    """Check if the password is correct, return True if it is, False otherwise."""
    username = request.form["username"]
    check = db.users.find_one({"username": username})

    if not check:
        # NOTE: this condition should not really occur, as the
        # username should be checked before.
        return False

    password = request.form["password"]
    hashed_password = hash_value(password)
    if hashed_password == check["password"]:
        sendmail(
            subject="Login on Flask Admin Boilerplate",
            sender="Flask Admin Boilerplate",
            recipient=check["email"],
            body="You successfully logged in on Flask Admin Boilerplate",
        )
        session["username"] = username
        return True
    return False


def register_user() -> bool:
    """Register a new user, and send a confirmation email."""
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    user_data = json.loads(json_util.dumps(data))
    user_data["password"] = hash_value(user_data["password"])
    user_data["confirmpassword"] = hash_value(user_data["confirmpassword"])

    assert (
        user_data["password"] == user_data["confirmpassword"]
    ), "Passwords do not match"

    user_data["created_at"] = datetime.now(tz=timezone.utc)
    if db.users.insert(user_data):
        sendmail(
            subject="Registration for Flask Admin Boilerplate",
            sender="Flask Admin Boilerplate",
            recipient=user_data["email"],
            body="You successfully registered on Flask Admin Boilerplate",
        )
        return True
    return False
