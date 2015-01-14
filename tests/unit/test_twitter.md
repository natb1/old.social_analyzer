>>> import mock
>>> import social_analyzer.config
>>> social_analyzer.config.twitter_consumer_key = 'fake'
>>> social_analyzer.config.twitter_consumer_secret = 'fake'
>>> social_analyzer.config.twitter_access_token_key = 'fake'
>>> social_analyzer.config.twitter_access_token_secret = 'fake'
>>> import social_analyzer.social_workflows.twitter
>>> import social_analyzer.model
>>> identity = social_analyzer.model.Identity(twitter='StephenAtHome')
>>> observable_workflow = mock.MagicMock()
>>> with mock.patch('social_analyzer.social_workflows.twitter.api') as mock_api:
...     with mock.patch('social_analyzer.social_workflows.twitter._get_urls') as mock_urls:
...         mock_urls.return_value = ['evil.example.com', 'benign.example.com']
...         social_analyzer.social_workflows.twitter.social_workflow(
...             identity, observable_workflow)
...         mock_api.method_calls
...         len(observable_workflow.delay.call_args_list)
[call.GetUserTimeline(screen_name='StephenAtHome')]
2
