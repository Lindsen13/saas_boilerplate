"""Test implementation of the mail module."""

from utils.mail import sendmail
import pytest


@pytest.mark.parametrize(
    "subject, sender, recipient, body",
    [
        ("Test", "Test", "Test", "Test"),
        (
            "Test email",
            "ivo.lindsen@email.com",
            "customer@email.com",
            "This is a test email",
        ),
    ],
)
def test_sendmail(subject: str, sender: str, recipient: str, body: str):
    """Test the sendmail function."""
    assert sendmail(subject, sender, recipient, body)
