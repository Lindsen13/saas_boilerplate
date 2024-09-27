import mock
import pytest


def test_register(client):
    """Test the register view."""
    response = client.get("/register")
    assert b'<h1 class="h4 text-gray-900 mb-4">Create an Account!</h1>' in response.data


def test_register_post(client):
    """Test the register view when posting data."""
    with mock.patch("views.auth.register_user", mock.MagicMock()) as mock_register_user:
        response = client.post("/register", follow_redirects=True)
        assert b'<h1 class="h4 text-gray-900 mb-4">Welcome Back!</h1>' in response.data
        assert mock_register_user.assert_called_once


def test_login(client):
    """Test the login view."""
    response = client.get("/login")
    assert b'<h1 class="h4 text-gray-900 mb-4">Welcome Back!</h1>' in response.data


def test_login_authenticated(authenticated_client):
    """Test the login view when authenticated."""
    response = authenticated_client.get("/login", follow_redirects=True)
    assert b'<h1 class="h3 mb-0 text-gray-800">Dashboard</h1>' in response.data


@pytest.mark.parametrize("exists, expected", [(True, b"true"), (False, b"false")])
def test_check_user_login_false(client, exists: bool, expected: str):
    """Test the check_user_login view."""
    with mock.patch(
        "views.auth.check_username_exists", mock.MagicMock()
    ) as mock_check_username_exists:
        mock_check_username_exists.return_value = exists
        response = client.post("/check_username_exists")
        assert mock_check_username_exists.assert_called_once
        assert expected in response.data


@pytest.mark.parametrize("correct, expected", [(True, b"true"), (False, b"false")])
def test_check_user_password(client, correct: bool, expected: str) -> None:
    """Test the check_user_password view."""
    with mock.patch(
        "views.auth.check_login_password", mock.MagicMock()
    ) as mock_check_login_password:
        mock_check_login_password.return_value = correct
        response = client.post("/check_login_password")
        assert mock_check_login_password.assert_called_once
        assert expected in response.data


def test_forgot_password(client):
    """Test the forgot_password view."""
    response = client.get("/forgot_password")
    assert (
        b'<h1 class="h4 text-gray-900 mb-2">Forgot Your Password?</h1>' in response.data
    )


def test_update_name(authenticated_client):
    """test the update_name view."""
    updated_name = "NewName"
    with mock.patch(
        "views.auth.update_name_from_user", mock.MagicMock()
    ) as mock_update_name_from_user:
        response = authenticated_client.post(f"/update_name?name={updated_name}")
    assert response.data == b"true"
    assert mock_update_name_from_user.assert_called_once
