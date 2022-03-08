import pytest

def test_index(client):
    res = client.get('/tokens/')
    assert res.status_code == 200

def test_store(client):
    res = client.post('/tokens/', json={
        'name': ''
    })