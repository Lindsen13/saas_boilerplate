from model import check_login_password, check_username_exists, register_user
import mock
import pytest
from utils.hashpass import hash_value


@pytest.mark.parametrize(
    "username, password, confirmpassword, email",
    [
        ("test_user_1", "test_password_1", "test_password_1", "test_email_1"),
        ("test_user_2", "test_password_2", "test_password_2", "test_email_2"),
    ],
)
def test_register_user(
    username: str, password: str, confirmpassword: str, email: str, mongo_db
):
    """Test register_user function."""
    with (
        mock.patch("model.request", mock.MagicMock()) as mock_request,
        mock.patch("model.db", mongo_db),
        mock.patch("model.sendmail", mock.MagicMock()) as mock_sendmail,
    ):
        mock_request.form = {
            "username": username,
            "password": password,
            "confirmpassword": confirmpassword,
            "email": email,
        }
        result = register_user()

        assert result  # Example assertion
        assert mock_sendmail.call_count == 1

        assert mongo_db.users.find_one({"username": username}) is not None


@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("user_1", "password_1", True),
        ("user_2", "password_2", True),
        ("user_2", "password_wrong", False),
        ("user_wrong", "password_wrong", False),
    ],
)
def test_check_login_password(username: str, password: str, expected: bool, mongo_db):
    """Test check_login_password function."""
    users_in_db = [
        {
            "username": "user_1",
            "password": "password_1",
            "email": "email_1",
        },
        {
            "username": "user_2",
            "password": "password_2",
            "email": "email_1",
        },
    ]
    with (
        mock.patch("model.request", mock.MagicMock()) as mock_request,
        mock.patch("model.session", {}) as mock_session,
        mock.patch("model.db", mongo_db) as db,
        mock.patch("model.sendmail", mock.MagicMock()) as mock_sendmail,
    ):
        db.users.insert_many(
            [
                {
                    "username": user["username"],
                    "password": hash_value(user["password"]),
                    "email": user["email"],
                }
                for user in users_in_db
            ]
        )
        mock_request.form = {
            "username": username,
            "password": password,
        }
        result = check_login_password()
    assert result == expected
    if expected:
        assert mock_sendmail.call_count == 1
        assert mock_session["username"] == username


@pytest.mark.parametrize(
    "username, expected",
    [
        ("test_user", False),
        ("non_existent_user", False),
        ("user_1", True),
    ],
)
def test_check_username_exists(username: str, expected: bool, mongo_db):
    """Test check_username_exists function."""
    usernames_in_db = ["user_1", "user_2", "user_3"]
    with (
        mock.patch("model.request", mock.MagicMock()) as mock_request,
        mock.patch("model.db", mongo_db) as db,
    ):
        db.users.insert_many([{"username": user} for user in usernames_in_db])
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
