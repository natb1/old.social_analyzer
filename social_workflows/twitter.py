from __future__ import absolute_import

import urllib
import urllib2
import simplejson

import twitter

from social_analyzer.celery import celery
import social_analyzer.model
import social_analyzer.config

# one api per worker
api = twitter.Api(social_analyzer.config.twitter_consumer_key,
                  social_analyzer.config.twitter_consumer_secret,
                  social_analyzer.config.twitter_access_token_key,
                  social_analyzer.config.twitter_access_token_secret)

@celery.task
def social_workflow(identity, observable_workflow):
    statuses = api.GetUserTimeline(screen_name=identity.twitter)
    for url in _get_urls(statuses):
        observable = social_analyzer.model.Observable(url, identity)
        observable_workflow.delay(observable)

def _get_urls(statuses):
    for status in statuses:
        for url in status.urls:
            yield url.expanded_url
