>>> import mock
>>> import social_analyzer.tasks
>>> import social_analyzer.config
>>> social_analyzer.config.vt_key = '1fe0ef5feca2f84eb450bc3617f839e317b2a686af4d651a9bada77a522201b0'
>>> identity = social_analyzer.model.Identity(twitter='drEvil')
>>> observable = social_analyzer.model.Observable(value='evil.example.com',
...                                               attribution=identity)
>>> with mock.patch('social_analyzer.tasks._get_response') as mock_gr:
...     mock_gr.return_value = {'positives':6}
...     obs, indicated = social_analyzer.tasks.analyze(observable)
...     obs.value, indicated
('evil.example.com', True)
