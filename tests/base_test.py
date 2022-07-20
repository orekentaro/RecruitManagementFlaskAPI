class BaseTest:
    def login(self, client):
        with client:
            client.post(
                '/login', data={
                    "email": 'test@test.test',
                    "password": "password1234"
                    })
