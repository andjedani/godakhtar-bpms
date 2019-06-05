import re

REPLACES = (
    ('ي', 'ی'),
)


def is_time_stamp(l):
    if l[:2].isnumeric() and l[2] == ':':
        return True
    return False


def has_english_letters(line):
    if re.search('[a-zA-Z]', line):
        return True
    return False


def clean_up_lower(text):
    if text:
        result = text.lower().strip()
        return result
    return text


def clean_up(text):
    if text:
        result = text.strip()
        return result
    return text


def clean_up_alpha_numeric(text):
    if text:
        result = text.strip()
        return result
    return text
