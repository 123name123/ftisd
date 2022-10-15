import requests

r = requests.post('http://127.0.0.1:81/devide/', json={
    "dividend": 15,
    "divider": 3
})
print(r.status_code)
print(r.json())
