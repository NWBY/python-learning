import pytest

def test_index(client):
    res = client.get('/tokens')
    assert res.status_code == 200
