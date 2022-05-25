class BaseTest:
    def login(self, client):
        with client:
            client.post(
                '/user/login', data={
                    "email": 'kntru0218gj@gmail.com',
                    "password": "1234"
                    })
