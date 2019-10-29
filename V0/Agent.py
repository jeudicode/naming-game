import random
import string
import heapq
from word_generator import Word_Generator as wg

class Agent():

    def __init__(self, id, rule_set, many_objects, environment):
        self.environment = environment
        self.id = id
        self.rule_set = rule_set
        self.objects = []
        for i in range(many_objects):
            self.objects.append([])

    def communicateFirstStage(self, agent_id):
        # Communicate with other agent
        # Select a random Object to speak
        id_object = random.randrange(0, len(self.objects))

        # If our memory is empty, generate new word
        if (len(self.objects[id_object]) == 0):
            self.generateOwnWord(id_object)
        
        # Select word with the highest frequency
        word = heapq.nlargest(1, self.objects[id_object])[0][1]
        
        # If the hearer knows the word, the communication is successful
        if (self.environment.communities[self.rule_set - 1].agents[agent_id].knowsWord(id_object, word) == 1):
            self.environment.communities[self.rule_set - 1].agents[agent_id].reduceAllWordsBut(id_object, word)
        else: 
            # Else the hearer learns the word
            self.environment.communities[self.rule_set - 1].agents[agent_id].learnWord(id_object, word)
    
    def generateOwnWord(self, id_object):
        generated_words = wg.generate_words(1, self.rule_set)
        self.objects[id_object].append((1, generated_words[0]))
        heapq.heapify(self.objects[id_object])
              
    
    def knowsWord(self, id_object, word):
        for i in range(len(self.objects[id_object])):
            if (word == self.objects[id_object][i][1]):
                return True
        return False
    
    def reduceAllWordsBut(self, id_object, word):
        new_words = []
        for i in range(len(self.objects[id_object])):
            if (word == self.objects[id_object][i][1]):
                new_words.append((self.objects[id_object][i][0] + 1, word))
            elif (int((self.objects[id_object][i][0] / 16)) >= 1):
                new_words.append((int(self.objects[id_object][i][0] / 16), word))
        self.objects[id_object] = new_words

        heapq.heapify(self.objects[id_object])
    
    def learnWord(self, id_object, word):
        # print(self.objects[id_object])
        heapq.heappush(self.objects[id_object], (1, word)) 