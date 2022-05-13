from tpass_parsers.celery import app
from .services import search

@app.task
def parse_pass_all():
    search()