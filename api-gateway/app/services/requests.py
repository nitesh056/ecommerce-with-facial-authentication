import requests


def get(path):
    r = requests.get('http://127.0.0.1:8000/api'+path)
    return r.json(), r.status_code == requests.codes.ok
    

def post(path, payload):
    r = requests.post('http://127.0.0.1:8000/api'+path, json=payload)
    return r.json(), r.status_code == requests.codes.ok