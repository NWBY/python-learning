from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from distroly.auth import login_required
from distroly.db import get_db

bp = Blueprint('distro', __name__)

@bp.route('/')
def index():
    db = get_db()

    distros = db.execute(
        'SELECT d.id, name, description, created, user_id, username'
        ' FROM distros d JOIN users u ON d.user_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('distro/index.html', distros=distros)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        error = None

        if not name:
            error = 'Name is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO distros (name, description, user_id)'
                ' VALUES (?, ?, ?)',
                (name, description, g.user['id'])
            )
            db.commit()

            return redirect(url_for('distro.index'))

    return render_template('distro/create.html')