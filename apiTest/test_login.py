import unittest, requests, json

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'https://api.movtile.com/account-service/login'
        cls.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8'
        }

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login_wuwp(self):
        
        data = {
            'username': '17396873453',
            'password': '11111111',
            'appId': '11',
            'appClientType': 'WEB'
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        response = response.json()
        code = response['code']
        self.assertEqual(code, 200)

if __name__ == '__main__':
    unittest.main()