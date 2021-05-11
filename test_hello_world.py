#from hello import app
#with app.test_client() as c:
#    response = c.get('/')
#    assert response.data == b'Hello World!'
#    assert response.status_code == 200


import hello
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = hello.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_message(self):
        response = self.app.get('/')
        message = hello.wrap_html('Hello DockerCon 2018!')
        self.assertEqual(response.data, message)

if __name__ == '__main__':
    unittest.main()
