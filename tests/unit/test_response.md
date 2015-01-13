>>> import mock
>>> import social_analyzer.tasks
>>> smtp_server = 'smtp.example.com'
>>> identity = social_analyzer.model.Identity(twitter='drEvil')
>>> observable = social_analyzer.model.Observable(value='evil.example.com',
...                                               attribution=identity)
>>> with mock.patch('smtplib.SMTP') as MockSMTP:
...     social_analyzer.tasks._respond(observable, 'nathan@natb1.com',
...                                    'role@example.com', smtp_server)
...     MockSMTP.assert_called_once_with(smtp_server)
...     MockSMTP.return_value.quit.assert_called_once_with()
...     MockSMTP.return_value.sendmail.call_args
call('nathan@natb1.com', ['role@example.com'], 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nSubject: found indicator\nFrom: nathan@natb1.com\nTo: role@example.com\n\nevil: twitter drEvil -> evil.example.com')
