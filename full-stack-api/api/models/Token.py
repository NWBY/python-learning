from api import db

class Token(db.Model):
    
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
    created_at = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False,
        server_default=db.func.now()
    )
    
    def __repr__(self):
        return '<Token {}>'.format(self.name)