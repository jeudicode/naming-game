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
        if (self.environment.communities[self.rule_set - 1].agents[agent_id].knowsWord(id_object, word)):
            self.environment.communities[self.rule_set - 1].agents[agent_id].reduceAllWordsBut(id_object, word)
        else: 
            # Else the hearer learns the word
            self.environment.communities[self.rule_set - 1].agents[agent_id].learnWord(id_object, word)
    
    def generateOwnWord(self, id_object):
        generated_words = wg.generate_words(1, self.rule_set)
        self.objects[id_object].append((1, generated_words[0], len(generated_words[0])))
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
                new_words.append((self.objects[id_object][i][0] + 1, word, len(word)))
            elif (int((self.objects[id_object][i][0] / 16)) >= 1):
                new_words.append((int(self.objects[id_object][i][0] / 16), self.objects[id_object][i][1], len(self.objects[id_object][i][1])))
        self.objects[id_object] = new_words
        heapq.heapify(self.objects[id_object])
    
    def ambassadorCommunication(self, id_object, id_community):
        # Initialize parameters to ask preference
        own_word = self.objects[id_object][0][1]
        other_word = self.environment.communities[id_community].agents[0].objects[id_object][0][1]
        
        # Get preference of words 
        preference = self.getPreference(own_word, other_word)
        
        # If the agent prefers the other word it replaces its own
        if preference > self.objects[id_object][0][2]:
            self.objects[id_object][0] = (1, other_word, preference)

    def getPreference(self, own_word, other_word):
        # Initialize counters of how similar is the word to the current favourite one
        similar_letters = {}
        similar_pair_of_letters = {}
        n = len(own_word)
        for i in range(n):
            similar_letters[own_word[i]] = 1
            if i + 1 < n:
                similar_pair_of_letters[own_word[i] + own_word[i + 1]] = 1
        
        # Checks preference
        preference = 0
        n = len(other_word)
        for i in range(n):
            # Check if similar letter 
            if (other_word[i] in similar_letters):
                preference += 1
            # Check if similar pair of letters
            if (i + 1 < n):
                a = other_word[i] 
                b = other_word[i + 1] 
                c = a + b
                if (c in similar_pair_of_letters):
                    preference += 1
        return preference

    def saveFrequencies(self, id_object, id_community):
        # Checks if knows word
        cross_word = self.environment.communities[id_community].agents[0].objects[id_object][0][1]
        if (self.knowsWord(id_object, cross_word)):
            new_words = []
            for i in range(len(self.objects[id_object])):
                if (cross_word == self.objects[id_object][i][1]):
                    new_words.append((self.objects[id_object][i][0] + 1, self.objects[id_object][i][1], self.objects[id_object][i][2]))
                else:
                    new_words.append((self.objects[id_object][i][0], self.objects[id_object][i][1], self.objects[id_object][i][2]))
            self.objects[id_object] = new_words
        else:
            self.objects[id_object].append((1, cross_word, self.getPreference(self.objects[id_object][0][1], cross_word)))    

    def purgeLessFrequentWords(self, id_object):
        max_val = 0
        max_ele = 0
        for i in range(len(self.objects[id_object])):
            if (self.objects[id_object][i][0] > max_val):
                max_val = self.objects[id_object][i][0]
                max_ele = self.objects[id_object][i]
        self.objects[id_object] = [max_ele]

    def learnWord(self, id_object, word):
        # print(self.objects[id_object])
        heapq.heappush(self.objects[id_object], (1, word, len(word))) 