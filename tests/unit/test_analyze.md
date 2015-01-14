>>> import mock
>>> import social_analyzer.tasks
>>> identity = social_analyzer.model.Identity(twitter='drEvil')
>>> observable = social_analyzer.model.Observable(value='evil.example.com',
...                                               attribution=identity)
>>> fake_vt_key = '1fe0ef5feca2f84eb450bc3617f839e317b2a686af4d651a9bada77a522201b0'
>>> with mock.patch('social_analyzer.tasks._get_response') as mock_gr:
...     mock_gr.return_value = {'positives':6}
...     obs, indicated = social_analyzer.tasks.analyze(observable, fake_vt_key)
...     obs.value, indicated
('evil.example.com', True)
