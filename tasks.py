from __future__ import absolute_import

from social_analyzer.celery import celery
import social_analyzer.model

@celery.task
def analyze(observable):
    return observable, True

@celery.task
def parse_analysis_and_respond(observable_analysis, *smtp_args):
    #TODO: sytactic issue with chaining arguments
    observable, analysis = observable_analysis
    evil = _parse(analysis)
    if evil:
        _respond(observable, *smtp_args)

def _parse(analysis):
    return analysis

import smtplib
from email.mime.text import MIMEText
template = 'evil: twitter {0} -> {1}'
def _respond(observable, from_address, to_address, smtp_server):
    body = template.format(observable.attribution.twitter,
                           observable.value)
    msg = MIMEText(body)
    msg['Subject'] = 'found indicator'
    msg['From'] = from_address
    msg['To'] = to_address
    s = smtplib.SMTP(smtp_server)
    s.sendmail(from_address, [to_address], msg.as_string())
    s.quit()
