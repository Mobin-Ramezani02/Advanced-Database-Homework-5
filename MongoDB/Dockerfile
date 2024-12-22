FROM python:3.12-alpine3.20

WORKDIR /app

COPY . .
# COPY /requirements.txt .

RUN pip install -r requirements.txt

CMD [ "fastapi", "run", "main.py" ]
