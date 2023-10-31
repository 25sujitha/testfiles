import pytest
import requests
import json


URL='http://localhost:5000'

def test_save_data():
    headers={'content-Type': 'application/json'}
    data={'key':'test-key','value':'test-value'}
    response = requests.post(f'{URL}/save',data=json.dumps(data),headers=headers)
    assert response.status_code == 200

def test_get_data():
    key='test-key'
    response = requests.post(f'{URL}/get?key={key}')
    data=response.json()
    assert response.status_code == 200
    assert data['source']=='database'

def test_get_data_not_found():
    key='non-exist'
    response = requests.post(f'{URL}/get?key={key}')
    assert response.status_code == 404

