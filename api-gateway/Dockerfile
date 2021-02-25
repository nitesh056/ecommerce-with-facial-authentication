FROM python:3

WORKDIR /usr/src/app/api-gateway

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]