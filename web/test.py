from flask_testing import TestCase
import unittest
from app.functions import get_information
from app import app


class TestFunctions(unittest.TestCase):
    def test_searching(self):
        self.assertTrue(get_information('hfjdncfj')['is_error'])
        self.assertEqual(get_information('kazan')['name'], 'Kazan')
        self.assertTrue(get_information('moscow')['temperature'])


class TestProject(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    def test_start(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('start.html')
    
    def test_choise_get(self):
        response = self.client.get('/choise')
        self.assert200(response)
        self.assertTemplateUsed('choise.html')
    
    def test_choice_post(self):
        response = self.client.post('/choise', data=dict(city='hfjskc'), follow_redirects=True)
        self.assert200(response)
        self.assertTemplateUsed('final.html')
        self.assertIn(b'Error getting weather foreast for Hfjskc, city not found', response.data)
    
    def test_cities(self):
        response = self.client.get('cities?city=kazan')
        self.assert200(response)
        self.assertTemplateUsed('final.html')
        self.assertIn(b'Weather forecast for city Kazan :', response.data)
    
    def test_cities_empty(self):
        response = self.client.get('cities?city=')
        self.assert200(response)
        self.assertIn(b'Weather forecast for city Kazan :', response.data)


if __name__ == '__main__':
    unittest.main()
