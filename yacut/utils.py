import random
from string import ascii_letters, digits

from yacut.models import URLMap

LETTERS_DIGITS = digits + ascii_letters


def get_unique_short_id():
    unique_short_id = ''.join(random.choices(LETTERS_DIGITS, k=6))
    if URLMap.query.filter_by(short=unique_short_id).first():
        unique_short_id = get_unique_short_id()
    return unique_short_id