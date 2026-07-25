import math
import re
from collections import Counter


def shannon_entropy(text: str) -> float:
    if not text:
        return 0

    counts = Counter(text)
    length = len(text)

    entropy = 0
    for count in counts.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy


def is_hex(text: str) -> bool:
    return bool(re.fullmatch(r"[0-9a-fA-F]+", text))


def is_base64(text: str) -> bool:
    return bool(
        re.fullmatch(
            r"[A-Za-z0-9+/=]+",
            text
        )
    )


def validate_ciphertext(text: str):

    text = text.strip()

    if len(text) < 16:
        return False, "Ciphertext is too short."

    entropy = shannon_entropy(text)

    if entropy < 3.0:
        return False, "Input has very low entropy and does not appear to be encrypted."

    if is_hex(text):
        return True, ""

    if is_base64(text):
        return True, ""

    if re.search(r"[A-Za-z]", text) and re.search(r"[0-9]", text):
        return True, ""

    return False, "Input does not appear to be valid ciphertext."