from datetime import datetime

from flask import url_for

from yacut import db
from yacut.constants import SHORT_STR


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(SHORT_STR), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Сериализатор, преобразование объекта модели в словарь"""
        return dict(
            url=self.original,
            short_link=url_for('redirect_view', custom_id=self.short,
                               _external=True),
        )

    def from_dict(self, data):
        """Десериализатор"""
        api_key = {'url': 'original', 'custom_id': 'short'}
        for field in api_key:
            if field in data:
                setattr(self, api_key[field], data[field])
