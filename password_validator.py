def is_valid_password(password):
    """
    Validates a password based on these rules:
    - Must be at least 8 characters long
    - Must contain at least one uppercase letter
    - Must contain at least one number
    - Must not contain spaces
    - Raises TypeError if input is not a string

    1) EP:

    password 7 characters long 
    password 8 characters long (valid)
    password 9 characters long (valid)
    password that is not string
    password that does not contain uppercase letter
    password that does not contain number
    password that contains space 

    2) bva
    7 chars invalid
    8 chars valid
    9 chars valid

    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if ' ' in password:
        return False
    return True