#import sys; sys.path.append('/opt/'
import social_analyzer.config

def setup_test(test):
    test.globs['twitter_screen_names'] = [
        'Nathan',
        'GhengisKhan',
        'drEvil',
        'MotherTeresa'
    ]
    social_analyzer.config.smtp_from = 'nathan@natb1.com'
    social_analyzer.config.smtp_to = 'role@example.com'
    social_analyzer.config.smtp_server = 'smtp.example.com'
    # (fake)
    social_analyzer.config.vt_key = '1fe0ef5feca2f84eb450bc3617f839e317b2a686af4d651a9bada77a522201b0'
    social_analyzer.config.smtp_server = 'smtp.example.com'
    social_analyzer.config.smtp_from = 'nathan@natb1.com'
    social_analyzer.config.smtp_to = 'role@example.com'
