from unittest import TestCase, main
from requests import post, get


class ServerTest(TestCase):
    def test_divide_200(self):
        req = post('http://127.0.0.1:81/devide/', json={
            "dividend": 15,
            "divider": 3
        })
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json(), 5.0)

    def test_divide_400(self):
        req1 = post('http://127.0.0.1:81/devide/', json={
            "dividend": 15,
            "divider": 0
        })
        self.assertEqual(req1.status_code, 400)
        req2 = post('http://127.0.0.1:81/devide/', json={
            "dividend": "saf",
            "divider": 4
        })
        self.assertEqual(req2.status_code, 400)

    def test_not_hello(self):
        req = post('http://127.0.0.1:81/something/')
        self.assertEqual(req.status_code, 405)

    def test_not_get_hello(self):
        req = post('http://127.0.0.1:81/hello/')
        self.assertEqual(req.status_code, 405)

    def test_right_hello(self):
        req = get('http://127.0.0.1:81/hello/')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.content.decode(), "HSE OneLove!")

    def test_set(self):
        req1 = get('http://127.0.0.1:81/set/', json={
            'key': "test_key",
            'value': "test_value"
        })
        self.assertEqual(req1.status_code, 405)
        req2 = post('http://127.0.0.1:81/set/', json={
            'key_': "test_key",
            'value': "test_value"
        })
        self.assertEqual(req2.status_code, 400)
        req3 = post('http://127.0.0.1:81/set/', json={
            'key': "test_key",
            'value_': "test_value"
        })
        self.assertEqual(req3.status_code, 400)
        req5 = post('http://127.0.0.1:81/set/')
        self.assertEqual(req5.status_code, 415)
        req4 = post('http://127.0.0.1:81/set/', json={
            'key': "test_key",
            'value': "test_value"
        })
        self.assertEqual(req4.status_code, 200)

    def test_get(self):
        req1 = post('http://127.0.0.1:81/get/')
        self.assertEqual(req1.status_code, 405)
        req2 = get('http://127.0.0.1:81/get/test/')
        self.assertEqual(req2.status_code, 404)
        req3 = post('http://127.0.0.1:81/set/', json={
            'key': "test",
            'value': "value"
        })
        self.assertEqual(req3.status_code, 200)
        req4 = get('http://127.0.0.1:81/get/test/')
        self.assertEqual(req4.status_code, 200)
        self.assertEqual(req4.json(), {'key': 'test', 'value': 'value'})


if __name__ == "__main__":
    main()
