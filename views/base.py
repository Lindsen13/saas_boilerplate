from flask import Blueprint, render_template, redirect, url_for, session
from utils.auth import login_required

base_bp = Blueprint('base', __name__)

@base_bp.route("/", methods=["GET"])
@login_required
def home():
    return render_template("index.html")

@base_bp.route("/logout", methods=["GET"])
@login_required
def logout():
    session.pop("username", None)
    return redirect(url_for("base.home"))

@base_bp.route("/404", methods=["GET"])
@login_required
def errorpage():
    return render_template("404.html")

@base_bp.route("/blank", methods=["GET"])
@login_required
def blank():
    return render_template("blank.html")

@base_bp.route("/buttons", methods=["GET"])
@login_required
def buttons():
    return render_template("buttons.html")

@base_bp.route("/cards", methods=["GET"])
@login_required
def cards():
    return render_template("cards.html")

@base_bp.route("/charts", methods=["GET"])
@login_required
def charts():
    return render_template("charts.html")

@base_bp.route("/tables", methods=["GET"])
@login_required
def tables():
    return render_template("tables.html")

@base_bp.route("/utilities-animation", methods=["GET"])
@login_required
def utilitiesanimation():
    return render_template("utilities-animation.html")

@base_bp.route("/utilities-border", methods=["GET"])
@login_required
def utilitiesborder():
    return render_template("utilities-border.html")

@base_bp.route("/utilities-color", methods=["GET"])
@login_required
def utilitiescolor():
    return render_template("utilities-color.html")

@base_bp.route("/utilities-other", methods=["GET"])
@login_required
def utilitiesother():
    return render_template("utilities-other.html")
