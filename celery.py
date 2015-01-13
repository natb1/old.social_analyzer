from __future__ import absolute_import

from celery import Celery

celery = Celery('social_analyzer.celery',
                broker='amqp://',
                backend='amqp://',
                include=['social_analyzer.tasks'])

# Optional configuration, see the application user guide.
celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    celery.start()
