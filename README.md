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
sudo chef-client -z -o social_analyzer
```
- `nosetests --with-doctest --doctest-extension=md --doctest-fixtures=-fixt /opt/social_analyzer/tests/examples`
```
