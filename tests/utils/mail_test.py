"""Test implementation of the mail module."""
from utils.mail import sendmail


def test_sendmail():
    """Test the sendmail function."""
    assert sendmail(
        subject="Test",
        sender="Test",
        recipient="",
        body="Test",
    )
