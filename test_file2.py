import pytest
from file2 import is_valid_email

@pytest.mark.parametrize("email", [
    "user@example.com",
    "user.name+tag+sorting@example.com",
    "user_name@example.co.uk",
    "user-name@sub.example.org",
    "user123@domain123.com",
    "u@d.io",
    "user.name@domain.co.in",
])
def test_is_valid_email_valid(email):
    assert is_valid_email(email) is True

@pytest.mark.parametrize("email", [
    "plainaddress",
    "@missingusername.com",
    "username@.com",
    "username@com",
    "username@domain..com",
    "username@domain,com",
    "username@domain",
    "username@domain.c",
    "username@.domain.com",
    "username@domain.com.",
    "",
    "user name@domain.com",
])
def test_is_valid_email_invalid(email):
    assert is_valid_email(email) is False