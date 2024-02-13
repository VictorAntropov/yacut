from string import ascii_letters, digits

LETTERS_DIGITS = digits + ascii_letters

ID_NOT_FOUND = 'Указанный id не найден'
REQUEST_BODY_MISSING = 'Отсутствует тело запроса'
URL_MUST_HAVE = '\"url\" является обязательным полем!'
SHORT_NAME = 'Указано недопустимое имя для короткой ссылки'
NAME_TAKEN = 'Имя "py" уже занято.'
SHORT_STR = 16

# Регулярное выражение для определения правильности имени для короткой ссылки
PATTERN_MATCH = r'^[a-zA-Z0-9]{1,16}$'
CREATE = 'Создать'
