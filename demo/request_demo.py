import  requests
def demo():

        url = 'http://127.0.0.1:8000/dar/user/login'


        data = {
            'user_name': 'test01',
            'password': 'admin123'
        }

        response = requests.post(url, data)

        print(response.text)

