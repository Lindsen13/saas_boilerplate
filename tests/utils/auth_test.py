from utils.auth import login_required
import mock


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
