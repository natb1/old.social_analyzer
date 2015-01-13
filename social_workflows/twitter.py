from __future__ import absolute_import

from social_analyzer.celery import celery
import social_analyzer.model

@celery.task
def social_workflow(identity, observable_workflow):
    observables = [
        social_analyzer.model.Observable('1.1.1.1', identity),
        social_analyzer.model.Observable('2.2.2.2', identity)
    ]
    for observable in observables:
        observable_workflow.delay(observable)

