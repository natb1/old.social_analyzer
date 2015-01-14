from __future__ import absolute_import

from social_analyzer.celery import celery
import social_analyzer.model
import social_analyzer.config

url_report_endpoint = "https://www.virustotal.com/vtapi/v2/url/report"
@celery.task
def analyze(observable):
    parameters = {"resource": observable.value,
                  "apikey": social_analyzer.config.vt_key}
    response = _get_response(url_report_endpoint, parameters)
    #TODO: this is defensive programming. check the vt schema
    positives = response.get('positives', 0)
    indicated = positives > 5
    return observable, indicated

import simplejson
import urllib
import urllib2
def _get_response(url, parameters):
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url_report_endpoint, data)
    response = urllib2.urlopen(req)
    json = response.read()
    response_dict = simplejson.loads(json)
    return response_dict

import smtplib
from email.mime.text import MIMEText
@celery.task
def respond(observable_indicated):
    #TODO: sytactic issue with chaining arguments
    observable, indicated = observable_indicated
    if indicated:
        _send_email(observable)

template = 'evil: twitter {0} -> {1}'
def _send_email(observable):
    body = template.format(observable.attribution.twitter,
                           observable.value)
    msg = MIMEText(body)
    msg['Subject'] = 'found indicator'
    msg['From'] = social_analyzer.config.smtp_from
    msg['To'] = social_analyzer.config.smtp_to
    s = smtplib.SMTP(social_analyzer.config.smtp_server)
    s.sendmail(social_analyzer.config.smtp_from,
               [social_analyzer.config.smtp_to],
               msg.as_string())
    s.quit()
