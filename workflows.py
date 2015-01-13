from __future__ import absolute_import

from celery import group, chain

import social_analyzer.tasks
#TODO: import all social workflows
import social_analyzer.social_workflows.twitter

def init_twitter_workflow(screen_names, *smtp_args):
    social_wf = social_analyzer.social_workflows.twitter.social_workflow
    observable_wf = chain(
        social_analyzer.tasks.analyze.s(),
        social_analyzer.tasks.parse_analysis_and_respond.s(*smtp_args))
    twitter_wf = group(
        social_wf.s(social_analyzer.model.Identity(twitter=sn), observable_wf)
        for sn in screen_names
    )
    twitter_wf.apply_async()

