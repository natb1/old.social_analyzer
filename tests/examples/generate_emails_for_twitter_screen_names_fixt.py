import sys; sys.path.append('/opt/') #TODO: hack

def setup_test(test):
    test.globs['twitter_screen_names'] = [
        'Nathan',
        'GhengisKhan',
        'drEvil',
        'MotherTeresa'
    ]
    test.globs['fake_vt_key'] = '1fe0ef5feca2f84eb450bc3617f839e317b2a686af4d651a9bada77a522201b0'
