from api import celery

@celery.task()
def update_token():