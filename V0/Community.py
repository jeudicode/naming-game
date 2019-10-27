from Agent import Agent
import random
import string 

class Comunity():

    def __init__(self, id, rule_set, many_objects, many_agents, environment):
        self.environment = environment
        self.id = id
        self.rule_set = rule_set
        # Populate agents
        self.agents = []
        for i in range(many_agents):
            self.agents.append(Agent(i, rule_set, many_objects, environment))

    def communicate(self, agent_id):
        # Communicate with other agent
        # If our memory is empty, generate new word
        if (len(self.words) == 0):
            self.generateOwnWord()
        
        # Select Random word from the memory of the agent
        id_word = random.randrange(0, len(self.words))
        
        # If the hearer knows the word, the communication is successful
        if (self.environment.agents[agent_id].knowsWord(self.words[id_word]) == 1):
            self.environment.agents[agent_id].removeAllWordsBut(self.words[id_word])
            self.removeAllWordsBut(self.words[id_word])
        else: 
            # Else the hearer learns the word
            self.environment.agents[agent_id].learnWord(self.words[id_word])
    
    def generateOwnWord(self,):
        alphabet = string.ascii_lowercase
        newWord = ""
        for i in range(4):
            newWord += alphabet[random.randrange(0, len(alphabet))]
        self.words.append(newWord)
    
    def knowsWord(self, word):
        for i in range(len(self.words)):
            if (word == self.words[i]):
                return True
        return False
    
    def removeAllWordsBut(self, word):
        self.words = []
        self.words.append(word)
    
    def learnWord(self, word):
        self.words.append(word)