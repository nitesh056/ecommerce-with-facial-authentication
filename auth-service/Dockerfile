FROM python:3

WORKDIR /usr/src/app/auth-service

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]