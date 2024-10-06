import unittest
from app import app

app = app.test_client()

def test_helloworld():
    response = app.get('/')
    assert response.status_code == 200

def test_new():
    response = app.get('/new?q=1&length=10')
    assert response.status_code == 200

def test_onePass():
    response = app.get('/1pass')
    assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()