from __future__ import absolute_import

from social_analyzer.celery import celery
import social_analyzer.model

url_report_endpoint = "https://www.virustotal.com/vtapi/v2/url/report"
@celery.task
def analyze(observable, vt_key):
    parameters = {"resource": observable.value,
                  "apikey": vt_key}
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
def respond(observable_indicated, *smtp_args):
    #TODO: sytactic issue with chaining arguments
    observable, indicated = observable_indicated
    if indicated:
        _send_email(observable, *smtp_args)

template = 'evil: twitter {0} -> {1}'
def _send_email(observable, from_address, to_address, smtp_server):
    body = template.format(observable.attribution.twitter,
                           observable.value)
    msg = MIMEText(body)
    msg['Subject'] = 'found indicator'
    msg['From'] = from_address
    msg['To'] = to_address
    s = smtplib.SMTP(smtp_server)
    s.sendmail(from_address, [to_address], msg.as_string())
    s.quit()
