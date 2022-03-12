from flask import (
    Blueprint, request, jsonify, abort
)
from api.models.Token import Token
from api import db

bp = Blueprint('token', __name__, url_prefix='/tokens')

@bp.route('/')
def index():
    allTokens = Token.query.all()
        
    return jsonify(allTokens)

@bp.route('/', methods=['POST'])
def store():
    data = request.json
    
    name = data.get('name')
    unit_name = data.get('unit_name')
    description = data.get('description')
    total_supply = data.get('total_supply')
    
    token = Token(
        name=name,
        unit_name=unit_name,
        description=description,
        total_supply=total_supply,
        market_cap=0
    )
    db.session.add(token)
    db.session.commit()
    
    return jsonify(token.json_format())

@bp.route('/<unit_name>')
def show(unit_name):
    token = Token.query.filter_by(unit_name=unit_name).first()
    
    if token is None:
        abort(404)
    
    return jsonify(token.json_format())

@bp.route('/<unit_name>', methods=['PUT'])
def update(unit_name):
    token = Token.query.filter_by(unit_name=unit_name).first()
    
    if token is None:
        abort(404)
        
    data = request.json
    
    for key, value in data.items():
        setattr(token, key, value)
    
    db.session.commit()
    
    return jsonify(token.json_format())