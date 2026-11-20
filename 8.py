# Experiment 8: Check whether a given string is a valid identifier
import keyword
import string


def is_valid_identifier(s):
    """Manual check following Python's naming rules."""
    if not s:
        return False, "string is empty"
    if keyword.iskeyword(s):
        return False, "it is a reserved keyword"
    if s[0] not in string.ascii_letters + "_":
        return False, "must start with a letter or underscore"
    for ch in s:
        if ch not in string.ascii_letters + string.digits + "_":
            return False, f"contains invalid character {ch!r}"
    return True, "valid identifier"


while True:
    text = input("\nEnter a string (or 'quit' to exit): ")
    if text.lower() == "quit":
        break
    ok, reason = is_valid_identifier(text)
    print(f"'{text}' -> {'VALID' if ok else 'INVALID'} ({reason})")
    # cross-check with the built-in method
    builtin = text.isidentifier() and not keyword.iskeyword(text)
    print("Built-in isidentifier() check agrees:", builtin == ok)
