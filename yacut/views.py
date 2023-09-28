from flask import flash, redirect, render_template

from yacut import app, db
from yacut.forms import YaCutForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = YaCutForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    short_name = form.custom_id.data

    if URLMap.query.filter_by(short=short_name).first():
        flash(f'Имя {short_name} уже занято!')
        return render_template('index.html', form=form)

    if not short_name:
        short_name = get_unique_short_id()

    url_map = URLMap(
        original=form.original_link.data,
        short=short_name,
    )
    db.session.add(url_map)
    db.session.commit()
    return render_template('index.html', form=form, short=short_name)


@app.route('/<string:custom_id>', methods=('GET',))
def redirect_view(custom_id):
    return redirect(
        URLMap.query.filter_by(short=custom_id).first_or_404().original)