from flask import Flask

from views.blueprints import views_bp

app = Flask(__name__)
app.register_blueprint(views_bp)

# secret key for user session
app.secret_key = "ITSASECRET"

if __name__ == "__main__":
    app.run(debug="true")
