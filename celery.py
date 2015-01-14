from __future__ import absolute_import

from celery import Celery

import social_analyzer.social_workflows

include = ['social_analyzer.tasks'] 
include.extend('social_analyzer.social_workflows.'+sw
               for sw in social_analyzer.social_workflows.__all__)
celery = Celery('social_analyzer.celery',
                broker='amqp://',
                backend='amqp://',
                include=include)

celery.conf.CELERY_TASK_RESULT_EXPIRES=3600
celery.conf.CELERY_ROUTES = {
    'social_analyzer.tasks.analyze': {'queue': 'analyze'},
    'social_analyzer.tasks.respond': {'queue': 'respond'},
    'social_analyzer.social_workflows.twitter.social_workflow': {
        'queue': 'twitter'
    },
}

if __name__ == '__main__':
    celery.start()
