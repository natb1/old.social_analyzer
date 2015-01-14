```
>>> twitter_screen_names
['Nathan', 'GhengisKhan', 'drEvil', 'MotherTeresa']
>>> import social_analyzer.workflows
>>> social_analyzer.workflows.init_twitter_workflow(twitter_screen_names) 
call('nathan@natb1.com', ['role@example.com'], 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nSubject: found indicator\nFrom: nathan@natb1.com\nTo: role@example.com\n\nevil: twitter drEvil -> evil.example.com')
call('nathan@natb1.com', ['role@example.com'], 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nSubject: found indicator\nFrom: nathan@natb1.com\nTo: role@example.com\n\nevil: twitter GhengisKhan -> evil.example.com')

```
