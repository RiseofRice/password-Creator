import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_new_get(self):
        response = self.app.get('/new?q=5&length=10')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success.html', response.data)

    def test_new_post(self):
        response = self.app.post('/new', data=dict(q=5, length=10))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success.html', response.data)

if __name__ == '__main__':
    unittest.main()