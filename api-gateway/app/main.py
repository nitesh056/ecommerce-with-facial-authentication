from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        payload = {
            'user': {
                'email': request.form['email'],
                'password': request.form['password']
            }
        }

        r = requests.post('http://auth-service:8000/api/u/login', json=payload)

        result = r.json()
        if r.status_code == requests.codes.ok:
            return result['token']
        else:
            return result['detail']
            return render_template('index.html', payload={
                "email": request.form['email']
            })

    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
