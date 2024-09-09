from flask import request, session
from utils.database import db
from utils.hashpass import getHashed
from utils.mail import sendmail
from bson import json_util
from datetime import datetime, timezone
import json


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
    password = request.form["password"]
    hashpassword = getHashed(password)
    if hashpassword == check["password"]:
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
    user_data["password"] = getHashed(user_data["password"])
    user_data["confirmpassword"] = getHashed(user_data["confirmpassword"])
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
