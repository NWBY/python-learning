import datetime
from api import db
from dataclasses import dataclass

@dataclass
class Token(db.Model):
    id: int
    name: str
    unit_name: str
    description: str
    total_supply: int
    market_cap: int
    created_at: datetime
    
    __tablename__ = 'tokens'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    unit_name = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    description = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    total_supply = db.Column(
        db.BigInteger,
        nullable=True
    )
    market_cap = db.Column(
        db.BigInteger,
        nullable=True
    )
    created_at = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False,
        server_default=db.func.now()
    )
    
    def __repr__(self):
        return '<Token {}>'.format(self.name)
    
    def json_format(self):
        return {
            'name': self.name,
            'unit_name': self.unit_name,
            'description': self.description,
            'total_supply': self.total_supply,
            'market_cap': self.market_cap
        }