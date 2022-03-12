FROM python:alpine3.14

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY api .
COPY config.py config.py
COPY wsgi.py wsgi.py 
COPY .env .env

ENV FLASK_APP=wsgi
ENV FLASK_ENV=development

EXPOSE 5000

CMD [ "pwd" ]

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000" ]
# CMD [ "python" ]s