import pytest
from api import init_app, db

@pytest.fixture()
def app():
    app = init_app()
    app.config.update({
        "TESTING": True
    })
    
    yield app
    
@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()