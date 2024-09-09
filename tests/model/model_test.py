from unittest.mock import patch
import mongomock

# Import the functions to be tested
from model import check_login_password, check_username_exists, register_user
import mock

def test_register_user(mongo_db):
    # Your test code for register_user
    with (
        mock.patch("model.request", mock.MagicMock()) as mock_request,
        mock.patch("model.db", mongo_db) as db,
    ):
        mock_request.form = {
            "username": "test_user",
            "password": "test_password",
            "confirmpassword": "test_password",
            "email": "test_email",
        }
        result = register_user()
    assert result  # Example assertion


def test_check_login_password(mongo_db):
    # Your test code for check_login_password

    username = "test_user"
    password = "test_password"
    with (
        mock.patch("model.request", mock.MagicMock()) as mock_request,
        mock.patch("model.db", mongo_db) as db,
    ):
        db.users.insert_one(
            {
                "username": username,
                "password": password,
            }
        )
        mock_request.form = {
            "username": username,
            "password": password,
        }
        result = check_login_password()
    assert result is not None  # Example assertion

def test_check_username_exists(mongo_db):
    # Your test code for check_username_exists
    username = "test_user"
    with (
        mock.patch("model.request", mock.MagicMock()) as mock_request,
        mock.patch("model.db", mongo_db) as db,
    ):
        db.users.insert_one(
            {
                "username": username,
            }
        )
        mock_request.form = {
            "username": username,
        }
        result = check_username_exists()
        assert result is not None  # Example assertion
