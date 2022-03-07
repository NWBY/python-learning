from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    with app.app_context():
        # Register routes    
        
        # Register blueprints
        from .blueprints import token
        app.register_blueprint(token.bp)
        
        db.create_all()
        
        return app