from flask import Flask

def create_app():
    from views.auth import auth_bp
    from views.base import base_bp

    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(base_bp)

    # secret key for user session
    app.secret_key = "ITSASECRET"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug="true")
