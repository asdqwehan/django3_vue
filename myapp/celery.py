from __future__ import absolute_import
from celery import Celery

app = Celery(
    'myapp',
    broker = 'redis://127.0.0.1',
    backend = 'redis://127.0.0.1',
    include = ['myapp.tasks']
)

if __name__ == '__main__':
    app.start()