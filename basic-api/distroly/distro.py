from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from distroly.auth import login_required
from distroly.db import get_db

bp = Blueprint('distro', __name__)