import random
class Agent():
    words = []

    def __init__(self, id, environment):
        self.environment = environment
        self.id = id

    def communicate(self, agent_id):
        # Communicate with other agent
        # If our memory is empty, generate new word
        if (len(words) == 0):
            self.generateOwnWord()
        
        # Select Random word from the memory of the agent
        id_word = random.randrange(0, len(self.words) - 1)
        
        # If the hearer knows the word, the communication is successful
        if (self.environment.agents[agent_id].knowsWord(self.words[id_word]) == 1):
            self.environment.agents[agent_id].removeAllWordsBut(self.words[id_word])
            self.removeAllWordsBut(self.words[id_word])
        else: 
            # Else the hearer learns the word
            self.environment.agents[agent_id].learnWord(self.words[id_word])
    
    def generateOwnWord():
        newWord = ""
        