from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class YaCutForm(FlaskForm):
    original_link = URLField(
        'Оригинальная ссылка',
        validators=[DataRequired(message='Обязательно поле'),
                    ]
    )
    custom_id = StringField(
        'Вариант короткого идентификатора',
        validators=[Length(1, 16), Optional()]
    )
    submit = SubmitField('Создать')