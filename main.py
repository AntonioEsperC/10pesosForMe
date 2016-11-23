from naiveBayesClassifier import Classifier
from trainer import DataTrainer

if __name__ == '__main__':
    trainer = DataTrainer()

    lines = [line.rstrip('\n') for line in open('lyrics_10_1.txt')]
    title = True
    current_title = None
    for line in lines:
        if title:
            current_title = line.split(',')[1].strip()
            title = False
        elif line.strip() == '':
            title = True
        else:
            artist = ''.join(current_title.split())
            trainer.train(line, artist)

    classifier = Classifier(trainer)

    phrases = [line.rstrip('\n') for line in open('tests.txt')]
    for phrase in phrases:
        quote = phrase.split(',')[1]
        print phrase
        print classifier.classify(quote)
        print '\n'