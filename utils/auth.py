from dataclasses import dataclass
from datetime import datetime, timezone
from functools import wraps

from flask import redirect, request, session, url_for

from utils.database import db
from utils.hashpass import hash_value
from utils.mail import sendmail


@dataclass
class User:
    """Dataclass for User"""

    username: str
    email: str
    name: str
    hashed_password: str

    @classmethod
    def get_user(cls, username:str):
        """Get a user by username."""
        user = db.users.find_one({"username": username})
        if user:
            return cls(
                username=user["username"],
                email=user["email"],
                name=user["name"],
                hashed_password=user["password"],
            )
        return

    @classmethod
    def from_dict(cls, data: dict):
        """Initialize a User object from a dictionary."""
        return cls(
            username=data["username"],
            email=data["email"],
            name=data["name"],
            hashed_password=hash_value(data["password"]),
        )

    def create_user(self):
        """Create a new user."""
        user_data = {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "password": self.hashed_password,
            "created_at": datetime.now(tz=timezone.utc),
        }
        return db.users.insert(user_data)


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
    user = User.get_user(username=username)
    return True if user else False

def check_login_password() -> bool:
    """Check if the password is correct, return True if it is, False otherwise."""
    username = request.form["username"]
    user = User.get_user(username=username)

    if user:
        password = request.form["password"]
        hashed_password = hash_value(password)
        if hashed_password == user.hashed_password:
            sendmail(
                subject="Login on Flask Admin Boilerplate",
                sender="Flask Admin Boilerplate",
                recipient=user.email,
                body="You successfully logged in on Flask Admin Boilerplate",
            )
            session["username"] = username
            session["email"] = user.email
            session["name"] = user.name
            return True
    return False


def register_user() -> bool:
    """Register a new user, and send a confirmation email."""
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    user = User.from_dict(data)

    assert (
        user.hashed_password == hash_value(data["confirmpassword"])
    ), "Passwords do not match"

    if user.create_user():
        sendmail(
            subject="Registration for Flask Admin Boilerplate",
            sender="Flask Admin Boilerplate",
            recipient=user.email,
            body="You successfully registered on Flask Admin Boilerplate",
        )
        return True
    return False
