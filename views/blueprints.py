from flask import Blueprint, render_template, request, redirect, url_for, session

from model import checkloginusername, checkloginpassword, checkusername, register_user

views_bp = Blueprint('views', __name__)

@views_bp.route("/", methods=["GET"])
def home():
    if "username" in session:
        return render_template("index.html")
    else:
        return render_template("login.html")

# Register new user
@views_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        register_user()
        return redirect(url_for("views.login"))


# Check if email already exists in the registratiion page
@views_bp.route("/checkusername", methods=["POST"])
def check():
    return checkusername()


# Everything Login (Routes to renderpage, check if username exist and
# also verifypassword through Jquery AJAX request)
@views_bp.route("/login", methods=["GET"])
def login():
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("views.home"))


@views_bp.route("/checkloginusername", methods=["POST"])
def checkUserlogin():
    return checkloginusername()


@views_bp.route("/checkloginpassword", methods=["POST"])
def checkUserpassword():
    return checkloginpassword()


# The admin logout
@views_bp.route("/logout", methods=["GET"])  # URL for logout
def logout():  # logout function
    session.pop("username", None)  # remove user session
    return redirect(url_for("views.home"))  # redirect to home page with message


# Forgot Password
@views_bp.route("/forgot-password", methods=["GET"])
def forgotpassword():
    return render_template("forgot-password.html")


# 404 Page
@views_bp.route("/404", methods=["GET"])
def errorpage():
    return render_template("404.html")


# Blank Page
@views_bp.route("/blank", methods=["GET"])
def blank():
    return render_template("blank.html")


# Buttons Page
@views_bp.route("/buttons", methods=["GET"])
def buttons():
    return render_template("buttons.html")


# Cards Page
@views_bp.route("/cards", methods=["GET"])
def cards():
    return render_template("cards.html")


# Charts Page
@views_bp.route("/charts", methods=["GET"])
def charts():
    return render_template("charts.html")


# Tables Page
@views_bp.route("/tables", methods=["GET"])
def tables():
    return render_template("tables.html")


# Utilities-animation
@views_bp.route("/utilities-animation", methods=["GET"])
def utilitiesanimation():
    return render_template("utilities-animation.html")


# Utilities-border
@views_bp.route("/utilities-border", methods=["GET"])
def utilitiesborder():
    return render_template("utilities-border.html")


# Utilities-color
@views_bp.route("/utilities-color", methods=["GET"])
def utilitiescolor():
    return render_template("utilities-color.html")


# utilities-other
@views_bp.route("/utilities-other", methods=["GET"])
def utilitiesother():
    return render_template("utilities-other.html")
