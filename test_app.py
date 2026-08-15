import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_valid_order(client):
    response = client.get('/api/order/ORD-1001')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['order_id'] == 'ORD-1001'

def test_get_invalid_order(client):
    response = client.get('/api/order/ORD-9999')
    assert response.status_code == 404
    data = response.get_json()
    assert data['success'] == False

def test_get_return_policy(client):
    response = client.post('/api/returns', json={"category": "electronics"})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['category'] == 'Electronics'

def test_get_missing_json(client):
    response = client.post('/api/returns')
    assert response.status_code == 400
