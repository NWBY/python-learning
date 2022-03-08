import pytest
import json

from api.models.Token import Token

def test_index(client):
    res = client.get('/tokens/')
    assert res.status_code == 200

def test_store(client):
    data = {
        'name': 'Algorand',
        'unit_name': 'ALGO',
        'description': 'Pure Proof of Stake blockchain with a focus on security and building a decentralised future with the prospect of handling 10K+ TPS.',
        'total_supply': 10000000,
        'market_cap': 1000000000
    }
    
    res = client.post('/tokens/', json=data)
    resJson = json.loads(res.data)
    
    assert res.status_code == 200
    assert resJson == data
    
def test_show(app, client):
    token = Token(
        name='Algorand',
        unit_name='ALGO',
        description='Pure Proof of Stake blockchain with a focus on security and building a decentralised future with the prospect of handling 10K+ TPS.',
        total_supply=10000000,
        market_cap=1000000000
    )
    app.db.session.add(token)
    app.db.session.commit()
    
    res = client.get('/tokens/ALGO')
    resJson = json.loads(res.data)
    
    assert res.status_code == 200
    assert resJson['name'] == 'Algorand'
    