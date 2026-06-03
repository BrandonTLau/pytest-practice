import pytest
from password_validator import is_valid_password

'''
 """
    Validates a password based on these rules:
    - Must be at least 8 characters long
    - Must contain at least one uppercase letter
    - Must contain at least one number
    - Must not contain spaces
    - Raises TypeError if input is not a string


    test cases: 
    password 7 characters long 
    password 8 characters long (valid)
    password 9 characters long (valid)
    password that is not string
    password that does not contain uppercase letter
    password that does not contain number
    password that contains space 
'''


def test_password_too_short():
    #7 characters invalid
    is_valid = is_valid_password("49mF542")
    assert is_valid == False

def test_password_minimum_length():
    #8 characters long valid
    is_valid = is_valid_password("49mF542X")
    assert is_valid == True

def test_password_above_minimum_length():
    #9 characters long valid
    is_valid = is_valid_password("49mF542X!")
    assert is_valid == True

def test_password_not_string():
    #password is not string
    with pytest.raises(TypeError):
        is_valid_password(1234567890)

def test_password_no_uppercase():
    #password contains no uppercase 
    is_valid = is_valid_password("49mf542x!")
    assert is_valid == False

def test_password_no_number():
    is_valid = is_valid_password("abcdefgh")
    assert is_valid == False

def test_password_contains_space():
    is_valid = is_valid_password("49mF 542X")
    assert is_valid == False