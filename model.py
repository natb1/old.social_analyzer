class Identity:

    def __init__(self, twitter):
        self.twitter = twitter

class Observable:

    def __init__(self, value, identity):
        self.value = value
        self.attribution = identity
        
