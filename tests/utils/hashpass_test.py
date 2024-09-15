from utils.hashpass import hash_value
import pytest


@pytest.mark.parametrize(
    "password, expected_hash",
    [
        ("test_password", "6b1191e79536e629e87d08ac855f48c8"),
        ("903267e081ty3", "efa34fea7cf431a1044e364bca7735cf"),
        ("amacbookpro123", "5bd191ad29230753bc289ff451c30e7e"),
    ],
)
def test_hash_value(password: str, expected_hash: str):
    """test hash_value function."""
    assert hash_value(password) == expected_hash
