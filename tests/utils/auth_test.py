import mock
import pytest

from utils.auth import (
    check_login_password,
    check_username_exists,
    login_required,
    register_user,
    update_name_from_user,
    User,
)
from utils.hashpass import hash_value


def test_user_get_user(mongo_db) -> None:
    """Test User.get_user method."""
    expected_username = "test_user"
    expected_email = "test_email"
    expected_name = "test_name"
    expected_password = "test_password"
    with mock.patch("utils.auth.db", mongo_db):
        prep_user = User(
            username=expected_username,
            email=expected_email,
            name=expected_name,
            hashed_password=expected_password,
        )
        prep_user.create_user()
        user = User.get_user(expected_username)
    assert user.username == expected_username
    assert user.email == expected_email
    assert user.name == expected_name
    assert user.hashed_password == expected_password


def test_user_from_dict() -> None:
    """Test User.from_dict method."""
    user_dict = {
        "username": "test_user",
        "email": "test_email",
        "name": "test_name",
        "password": "test_password",
    }
    user = User.from_dict(user_dict)
    assert user.username == user_dict["username"]
    assert user.email == user_dict["email"]
    assert user.name == user_dict["name"]
    assert user.hashed_password == hash_value(user_dict["password"])


@pytest.mark.parametrize(
    "username, name, password, confirmpassword, email",
    [
        ("test_user_1", "user_1", "test_password_1", "test_password_1", "test_email_1"),
        ("test_user_2", "test_2", "test_password_2", "test_password_2", "test_email_2"),
    ],
)
def test_register_user(
    username: str, name: str, password: str, confirmpassword: str, email: str, mongo_db
):
    """Test register_user function."""
    with (
        mock.patch("utils.auth.request", mock.MagicMock()) as mock_request,
        mock.patch("utils.auth.db", mongo_db),
        mock.patch("utils.auth.sendmail", mock.MagicMock()) as mock_sendmail,
    ):
        mock_request.form = {
            "username": username,
            "name": name,
            "password": password,
            "confirmpassword": confirmpassword,
            "email": email,
        }
        result = register_user()

        assert result  # Example assertion
        assert mock_sendmail.call_count == 1

        assert mongo_db.users.find_one({"username": username}) is not None


def test_register_user_password_mismatch(mongo_db):
    """Test register_user function with password mismatch."""
    with (
        mock.patch("utils.auth.request", mock.MagicMock()) as mock_request,
        mock.patch("utils.auth.db", mongo_db),
        mock.patch("utils.auth.sendmail", mock.MagicMock()) as mock_sendmail,
    ):
        mock_request.form = {
            "username": "test_user",
            "password": "test_password",
            "name": "test_name",
            "confirmpassword": "test_password_wrong",
            "email": "test_email",
        }
        with pytest.raises(AssertionError):
            register_user()

        assert mock_sendmail.call_count == 0


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
        mock.patch("utils.auth.request", mock.MagicMock()) as mock_request,
        mock.patch("utils.auth.session", {}) as mock_session,
        mock.patch("utils.auth.db", mongo_db) as db,
        mock.patch("utils.auth.sendmail", mock.MagicMock()) as mock_sendmail,
    ):
        db.users.insert_many(
            [
                {
                    "username": user["username"],
                    "password": hash_value(user["password"]),
                    "email": user["email"],
                    "name": "just a name",
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
        assert mock_session["email"] is not None
        assert mock_session["name"] is not None


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
        mock.patch("utils.auth.request", mock.MagicMock()) as mock_request,
        mock.patch("utils.auth.db", mongo_db) as db,
    ):
        db.users.insert_many(
            [
                {
                    "username": user,
                    "name": "test_name",
                    "email": "test_email",
                    "password": "test_password",
                }
                for user in usernames_in_db
            ]
        )

        mock_request.form = {
            "username": username,
        }
        result = check_username_exists()
        assert result == expected


def test_login_required():
    """test the login_required decorator"""

    def protected_resource():
        return "This is a protected resource"

    with mock.patch("utils.auth.session", {"username": "test_user"}):
        assert login_required(protected_resource)() == "This is a protected resource"


def test_login_required_redirect():
    """test the login_required decorator when the user is not logged in"""

    def protected_resource():
        return "This is a protected resource"

    with (
        mock.patch("utils.auth.session", {}),
        mock.patch("utils.auth.url_for", mock.Mock()),
        mock.patch(
            "utils.auth.redirect", mock.Mock(return_value="redirected")
        ) as mock_redirect,
    ):
        assert login_required(protected_resource)() == "redirected"
        assert mock_redirect.assert_called_once


def test_update_name_from_user(mongo_db) -> None:
    """Test update_name_from_user function."""
    expected_username = "test_user"
    expected_name = "test_user"
    with (
        mock.patch("utils.auth.session", {}) as mock_session,
        mock.patch("utils.auth.db", mongo_db) as db,
    ):
        db.users.insert_one(
            {
                "username": expected_username,
                "password": "password",
                "email": "email",
                "name": "just a name",
            }
        )
        mock_session["username"] = expected_name
        result = update_name_from_user(
            username=expected_username, new_name=expected_name
        )

        got = db.users.find_one({"username": expected_username})

        assert result
        assert got["name"] == expected_name
