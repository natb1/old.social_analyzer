import sys; sys.path.append('/opt/') #TODO: hack

def setup_test(test):
    test.globs['twitter_screen_names'] = [
        'Nathan',
        'GhengisKhan',
        'drEvil',
        'MotherTeresa'
    ]
