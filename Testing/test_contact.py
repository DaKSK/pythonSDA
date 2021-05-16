'''
Task 1

1- Write a module (contact.py) and a class (Contact) with fields (name, home_phone, mobile_phone, email)
2- name and at least one phone number are required, the phones should have the country code.
3- Write the test cases:

    a- creating a Contact with name without any number
    b- creating a Contact with name and mobile phone using an invalid country_code
    c- creating a Contact with name and mobile phone using an invalid email

4- Properties and methods recommended:

    - home - returns the phone number without country code
    - mobile - returns the mobile number without country code
    - has_email() - returns True if the contact has an email
    - country - returns the country name for that phone number (+372 >> Estonia)
'''
from contact import Contact
import pytest


@pytest.fixture()
def valid_country_code():
    return "+372"


@pytest.fixture()
def invalid_country_code():
    return ""


@pytest.fixture()
def valid_name_input():
    return "John"


@pytest.fixture()
def valid_home_number_input():
    return "+3726310310"


@pytest.fixture()
def invalid_number_input():
    return "+0513545"


@pytest.fixture()
def valid_email_format():
    return "user@domain.com"


@pytest.fixture()
def invalid_email():
    return "domain.com"


@pytest.fixture()
def valid_mobile_number_input():
    return "+3725222471"


class TestCreateContact:

    def test_with_name_no_number(self, valid_name_input):
        # input
        name = valid_name_input

        # process
        with pytest.raises(ValueError):
            contact = Contact(name)

    # @pytest.mark.skip(reason="not yet implemented")
    def test_with_name_mobile_invalid_country_code(self, valid_name_input, invalid_number_input, valid_home_number_input):
        with pytest.raises(ValueError):
            contact = Contact(valid_name_input, home_phone=valid_home_number_input, mobile_phone=invalid_number_input)

    def test_with_invalid_email(self, valid_name_input, valid_mobile_number_input, invalid_email):
        contact = Contact(valid_name_input, mobile_phone=valid_mobile_number_input, email=invalid_email)
        assert contact.email == ""
