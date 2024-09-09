from flask import Blueprint, render_template, redirect, url_for, session

base_bp = Blueprint('base', __name__)

@base_bp.route("/", methods=["GET"])
def home():
    if "username" in session:
        return render_template("index.html")
    else:
        return render_template("login.html")


# The admin logout
@base_bp.route("/logout", methods=["GET"])  # URL for logout
def logout():  # logout function
    session.pop("username", None)  # remove user session
    return redirect(url_for("base.home"))  # redirect to home page with message


# 404 Page
@base_bp.route("/404", methods=["GET"])
def errorpage():
    return render_template("404.html")


# Blank Page
@base_bp.route("/blank", methods=["GET"])
def blank():
    return render_template("blank.html")


# Buttons Page
@base_bp.route("/buttons", methods=["GET"])
def buttons():
    return render_template("buttons.html")


# Cards Page
@base_bp.route("/cards", methods=["GET"])
def cards():
    return render_template("cards.html")


# Charts Page
@base_bp.route("/charts", methods=["GET"])
def charts():
    return render_template("charts.html")


# Tables Page
@base_bp.route("/tables", methods=["GET"])
def tables():
    return render_template("tables.html")


# Utilities-animation
@base_bp.route("/utilities-animation", methods=["GET"])
def utilitiesanimation():
    return render_template("utilities-animation.html")


# Utilities-border
@base_bp.route("/utilities-border", methods=["GET"])
def utilitiesborder():
    return render_template("utilities-border.html")


# Utilities-color
@base_bp.route("/utilities-color", methods=["GET"])
def utilitiescolor():
    return render_template("utilities-color.html")


# utilities-other
@base_bp.route("/utilities-other", methods=["GET"])
def utilitiesother():
    return render_template("utilities-other.html")
