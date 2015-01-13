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

## quickstart
- `git clone https://github.com/natb1/social_analyzer_infrastructure.git`
- [provision chefdk](https://downloads.chef.io/chef-dk/)
- deploy (locally):
```
berks vendor cookbooks -b social_analyzer_infrastructure/Berksfile
sudo chef-client -z -o social_analyzer_infrastructure
```
- `nosetests --with-doctest --doctest-extension=md --doctest-fixtures=_fixt /opt/social_analyzer/tests/examples`

## social workflows
Social workflows extend the way social_analyzer produces observables from
identities. Social workflows are modules in the social_workflows package.
They must implement a celery task called `social_workflow`. For example:
```
from __future__ import absolute_import

from social_analyzer.celery import celery

@celery.task
def social_workflow(identity, observable_workflow):
   rasie NotImplementedError()
```
where identity is an Identity, and observable_workflow is
a celery task that must be invoked once for each Observable instance.
