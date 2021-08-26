import json
from src.app import app

class TestHTTPResponses:
    '''
    Test the responses of the HTTP Request
    '''

    def test_one(self):
        '''
        Test a status code 200
        '''
        assert app.test_client().get('/london').status_code == 200

    def test_one(self):
        '''
        Test a status code 404
        '''
        response = app.test_client().get('/')
        json_response = json.loads(response.data.decode())
        assert json_response['errorCode'] == 404
        assert 'Route not found. Please, send a request with a value' in json_response['message']