import pytest
import food_service

def test_index():
    food_service.app.testing = True
    test_client = food_service.app.test_client()
    response = test_client.get('/')
    assert b'Food service' in response.data
