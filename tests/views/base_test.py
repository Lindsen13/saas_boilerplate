from typing import Final

WELCOME_MESSAGE: Final[bytes] = b'<h1 class="h4 text-gray-900 mb-4">Welcome Back!</h1>'


def test_request_example(client):
    """Test the request example view."""
    response = client.get("/", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_request_example_authenticated(authenticated_client) -> None:
    """Test the request example view when authenticated."""
    response = authenticated_client.get("/")
    assert b'<h1 class="h3 mb-0 text-gray-800">Dashboard</h1>' in response.data


def test_logout_authenticated(authenticated_client) -> None:
    """Test the logout function when authenticated."""
    response = authenticated_client.get("/logout", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data
    with authenticated_client.session_transaction() as session:
        assert session.get("username") is None


def test_logout_not_authenticated(client) -> None:
    """Test the logout function when not authenticated."""
    response = client.get("/logout", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_errorpage(authenticated_client) -> None:
    """Test the errorpage view."""
    response = authenticated_client.get("/404")
    assert b'<div class="error mx-auto" data-text="404">404</div>' in response.data


def test_errorpage_not_authenticated(client) -> None:
    """Test the errorpage view when not authenticated."""
    response = client.get("/404", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_blank(authenticated_client) -> None:
    """Test the blank view."""
    response = authenticated_client.get("/blank")
    assert b'<h1 class="h3 mb-4 text-gray-800">Blank Page</h1>' in response.data


def test_blank_not_authenticated(client) -> None:
    """Test the blank view when not authenticated."""
    response = client.get("/blank", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_buttons(authenticated_client) -> None:
    """Test the buttons view."""
    response = authenticated_client.get("/buttons")
    assert b'<h1 class="h3 mb-4 text-gray-800">Buttons</h1>' in response.data


def test_buttons_not_authenticated(client) -> None:
    """Test the buttons view when not authenticated."""
    response = client.get("/buttons", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_cards(authenticated_client) -> None:
    """Test the cards view."""
    response = authenticated_client.get("/cards")
    assert b'<h1 class="h3 mb-0 text-gray-800">Cards</h1>' in response.data


def test_cards_not_authenticated(client) -> None:
    """Test the cards view when not authenticated."""
    response = client.get("/cards", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_charts(authenticated_client) -> None:
    """Test the charts view."""
    response = authenticated_client.get("/charts")
    assert b'<h1 class="h3 mb-2 text-gray-800">Charts</h1>' in response.data


def test_charts_not_authenticated(client) -> None:
    """Test the charts view when not authenticated."""
    response = client.get("/charts", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_tables(authenticated_client) -> None:
    """Test the tables view."""
    response = authenticated_client.get("/tables")
    assert b'<h1 class="h3 mb-2 text-gray-800">Tables</h1>' in response.data


def test_tables_not_authenticated(client) -> None:
    """Test the tables view when not authenticated."""
    response = client.get("/tables", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_utilitiesanimation(authenticated_client) -> None:
    """Test the utilitiesanimation view."""
    response = authenticated_client.get("/utilities-animation")
    assert (
        b'<h1 class="h3 mb-1 text-gray-800">Animation Utilities</h1>' in response.data
    )


def test_utilitiesanimation_not_authenticated(client) -> None:
    """Test the utilitiesanimation view when not authenticated."""
    response = client.get("/utilities-animation", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_utilitiesborder(authenticated_client) -> None:
    """Test the utilitiesborder view."""
    response = authenticated_client.get("/utilities-border")
    assert b'<h1 class="h3 mb-1 text-gray-800">Border Utilities</h1>' in response.data


def test_utilitiesborder_not_authenticated(client) -> None:
    """Test the utilitiesborder view when not authenticated."""
    response = client.get("/utilities-border", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_utilitiescolor(authenticated_client) -> None:
    """Test the utilitiescolor view."""
    response = authenticated_client.get("/utilities-color")
    assert b'<h1 class="h3 mb-1 text-gray-800">Color Utilities</h1>' in response.data


def test_utilitiescolor_not_authenticated(client) -> None:
    """Test the utilitiescolor view when not authenticated."""
    response = client.get("/utilities-color", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data


def test_utilitiesother(authenticated_client) -> None:
    """Test the utilitiesother view."""
    response = authenticated_client.get("/utilities-other")
    assert b'<h1 class="h3 mb-1 text-gray-800">Other Utilities</h1>' in response.data


def test_utilitiesother_not_authenticated(client) -> None:
    """Test the utilitiesother view when not authenticated."""
    response = client.get("/utilities-other", follow_redirects=True)
    assert WELCOME_MESSAGE in response.data
