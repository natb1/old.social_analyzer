# social_analyzer

Solution that satisfies the requirement:

Generate an email alert for each url published by a list of twitter screen
names that is flagged by more than five vendors on virus total.

Given the following contraints:
- must use Python and Celery
- must use Twitter and VirusTotal public API
- must be extendable to other social networks
- must be distributable
- all IO must be non-blocking

## config
Integration tests require local load time config. Config parameters can be
found in config.py.

## social workflows
Social workflows extend the way social_analyzer produces observables from
identities. Social workflows are modules in the social_workflows package.
They must implement a celery task called `social_workflow`. For example:
```
from social_analyzer.celery import celery

@celery.task
def social_workflow(identity, observable_workflow):
   ...
   group(observable_workflow.s(o) for o in observables)()
```
where identity is an Identity, and observable_workflow is
a celery task that must be invoked once for each Observable instance.

Giving the social_workflow control over how the observable_workflow is
invoked is a deliberate design choice.

## assumptions
- Testing doesn't all work and generally not fully tested.
- Non-blocking IO is interpreted to mean guaranteed parallelism during IO.
This is enforced by using separate queues for IO bound tasks. A stricter
interpretation of non-blocking IO might require tasks to yield the worker
thread during IO.
- Rate limiting (and IO errors in general) are left unandled.

