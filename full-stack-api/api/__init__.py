from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    if os.environ.get('TESTING') == 'True':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevConfig')
    
    db.init_app(app)
    
    with app.app_context():
        # Register routes    
        
        # Register blueprints
        from .blueprints import token
        app.register_blueprint(token.bp)
        
        db.create_all()
        
        return app