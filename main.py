from naiveBayesClassifier import Classifier
from trainer import DataTrainer

if __name__ == '__main__':
    trainer = DataTrainer()

    #Lyrics file (Modify the string to try other test cases)
        #lyrics_10_1   -> test 1
        #lyrics_10_2   -> test 2
        #lyrics_10_10  -> test 3
    lines = [line.rstrip('\n') for line in open('lyrics_10_10.txt')]
    title = True
    current_title = None
    #Gets the class in case its the first line
    for line in lines:
        if title:
            current_title = line.split(',')[1].strip()
            title = False
        elif line.strip() == '':
            title = True
        else:
    #trains the model with each line of each song
            artist = ''.join(current_title.split())
            trainer.train(line, artist)

    #sends the data to the classifier
    classifier = Classifier(trainer)

    #tests all of the 20 phrases in tests.txt
    phrases = [line.rstrip('\n') for line in open('tests.txt')]
    for phrase in phrases:
        quote = phrase.split(',')[1]
        print phrase
    #prints the probabilities
        print classifier.classify(quote)
        print '\n'