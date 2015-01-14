```
>>> twitter_screen_names
['Nathan', 'GhengisKhan', 'drEvil', 'MotherTeresa']
>>> import social_analyzer.workflows
>>> social_analyzer.workflows.init_twitter_workflow(twitter_screen_names)
Called smtplib.SMTP('localhost')
Called smtp_connection.sendmail(
    'role@example.com',
    'To: role@example.com\nFrom: nathan@natb1.com\nSubject: indicator\n\nindicator evil.example.com in GhengisKhan twitter feed')
Called smtp_connection.sendmail(
    'role@example.com',
    'To: role@example.com\nFrom: nathan@natb1.com\nSubject: indicator\n\nindicator evil.example.com in drEvil twitter feed')
Called smtp_connection.quit()

```
