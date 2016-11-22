import operator
from functools import reduce


class Classifier(object):
    """Classifies some text with respect to some trained data

    """
    def __init__(self, trainer):
        """
            Args:
                trainer(Trainer) The trainer object
        """
        self.data = trainer.data
        self.trainer = trainer
        self.prob = 0.0000001

    def classify(self, text):
        artists = self.data.get_artists()

        # need to have unique tokens
        tokens = list(set(self.trainer.tokenize_text(text)))

        artists_probability = {}

        for artist_name in artists:
            # P(token_1|artist_i)
            tokens_prob =\
                [self.get_token_prob(token, artist_name) for token in tokens]
            # P(token_1|artist_i) * ... * P(token_n|artist_i)
            try:
                token_prob =\
                    reduce(lambda a, b: a*b, (i for i in tokens_prob if i))
            except:
                token_prob = 0
            artists_probability[artist_name] =\
                token_prob * self.get_prior(artist_name)
        return sorted(artists_probability.items(),
                      key=operator.itemgetter(1),
                      reverse=True)

    def get_prior(self, name):
        return self.data.get_artist_count(name) / self.data.get_count()

    def get_token_prob(self, token, artist_name):
        # P(token|artist_i)
        artist_count = self.data.get_artist_count(artist_name)

        try:
            token_freq = self.data.get_frequency(token, artist_name)
        except:
            return None

        if token_freq is None:
            return self.prob

        return token_freq / artist_count
