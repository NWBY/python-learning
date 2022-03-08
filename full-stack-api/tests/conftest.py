import pytest
import os
from api import init_app, db

@pytest.fixture()
def app(monkeypatch):
    monkeypatch.setenv('TESTING', 'True')

    app = init_app()
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
    
@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()