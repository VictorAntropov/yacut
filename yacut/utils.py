import random

from yacut.constants import LETTERS_DIGITS
from yacut.models import URLMap


def get_unique_short_id():
    """Формирование коротких идентификаторов переменной длины. """
    unique_short_id = ''.join(random.choices(LETTERS_DIGITS, k=6))
    if URLMap.query.filter_by(short=unique_short_id).first():
        unique_short_id = get_unique_short_id()
    return unique_short_id
