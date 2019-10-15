from word_generator import Word_Generator as wg

class Agent:

    words = []
    isAmbassador = False

    def __init__(self, number_of_objects, community):

        for i in range (number_of_objects):
            self.words.append(wg.generate_words(5, community))
    

    def getWords(self):
        return self.words
