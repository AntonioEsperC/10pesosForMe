import re


class Data(object):
    """Deals with the trained data

    """
    def __init__(self):
        self.artists_count = {}
        self.freq = {}

    def increase_artist(self, name):
        self.artists_count[name] = self.artists_count.get(name, 0) + 1

    def increase_token(self, token, name):
        if token not in self.freq:
            self.freq[token] = {}
        self.freq[token][name] = self.freq[token].get(name, 0) + 1

    def get_count(self):
        return float(sum(self.artists_count.values()))

    def get_artists(self):
        return self.artists_count.keys()

    def get_artist_count(self, name):
        return float(self.artists_count.get(name, None))

    def get_frequency(self, token, name):
        try:
            found_token = self.freq[token]
        except:
            #print "No frequency for token"
            raise

        try:
            return found_token[name]
        except:
            return None


class DataTrainer(object):
    """Trains some data to be used by the classifier
        Attibutes:
            data(Data) The trained data

    """
    def __init__(self, special_characters=['?!#%&']):
        """

        Args:
            special_characters (list, optional) List of special
            characters that shoul be removed

        """
        self.special_characters = special_characters
        self.data = Data()

    def tokenize_text(self, text):
        # lower is importan so that there is no difference
        # between same words in upper or lower case
        return text.lower().split(' ')

    def remove_special_characters(self, token):
        # remove special characters from a token
        return re.sub(str(self.special_characters), '', token)

    def train(self, text, artist_name):
        self.data.increase_artist(artist_name)
        tokens = self.tokenize_text(text)
        for token in tokens:
            token = self.remove_special_characters(token)
            self.data.increase_token(token, artist_name)
