from datetime import datetime

from flask import url_for

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_view', custom_id=self.short, _external=True),
        )

    def from_dict(self, data):
        api_key = {'url': 'original', 'custom_id': 'short'}
        for field in api_key:
            if field in data:
                setattr(self, api_key[field], data[field])