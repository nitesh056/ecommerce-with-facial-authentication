import requests, os

URL_PREFIX = '/api'


def get(url, path):
    r = requests.get(os.environ.get(url) + URL_PREFIX + path)
    return r.json(), r.status_code == requests.codes.ok
    

def post(url, path, payload):
    r = requests.post(os.environ.get(url) + URL_PREFIX + path, json=payload)
    return r.json(), r.status_code == requests.codes.ok


def put(url, path, payload):
    r = requests.put(os.environ.get(url) + URL_PREFIX + path, json=payload)
    return r.json(), r.status_code == requests.codes.ok
    

def delete(url, path):
    r = requests.delete(os.environ.get(url) + URL_PREFIX + path)
    return r.json(), r.status_code == requests.codes.ok
