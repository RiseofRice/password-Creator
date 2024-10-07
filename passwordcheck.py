def check_password(password):
    """
    Evaluates the strength of a given password and provides reasons for its strength rating.

    Parameters:
    password (str): The password to be evaluated.

    Returns:
    tuple: A tuple containing:
        - strength (str): The strength of the password ("weak" or "strong").
        - reasons (list): A list of reasons explaining why the password is considered weak.
    """
    strength = "weak"
    reasons = []

    if len(password) < 10:
        if any(char.isdigit() for char in password):
            if any(char.isupper() for char in password):
                if any(char.islower() for char in password):
                    if any(char in "!@#$%^&*()-+" for char in password):
                        strength = "strong"
                    else:
                        reasons.append("password does not contain special characters")
                else:
                    reasons.append("password does not contain lowercase characters")
            else:
                reasons.append("password does not contain uppercase characters")
        else:
            reasons.append("password does not contain digits")
    else:
        reasons.append("password is too short")

    return strength, reasons