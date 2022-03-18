from urllib import request
from api import celery, db
import requests

@celery.task()
def update_token():
    res = requests.get()