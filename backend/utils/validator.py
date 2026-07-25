import re

def validate_ciphertext(ciphertext: str):
    ciphertext = ciphertext.strip()

    if not ciphertext:
        return False, "Ciphertext cannot be empty."

    if " " in ciphertext:
        return False, "Ciphertext should not contain spaces."

    if len(ciphertext) < 16:
        return False, "Ciphertext is too short."

    if re.search(r"[^A-Za-z0-9+/=]", ciphertext):
        return False, "Ciphertext contains unsupported characters."

    return True, ""