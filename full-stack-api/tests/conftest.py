import pytest
from api import init_app, db

@pytest.fixture()
def app():
    app = init_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": 'postgresql://test:secret@localhost:5435/token-tracker-test'
    })
    
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