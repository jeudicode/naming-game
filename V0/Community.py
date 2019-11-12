from Agent import Agent
import random
import string 

class Community():

    def __init__(self, id, many_objects, many_agents, environment):
        self.environment = environment
        self.id = id
        self.rule_set = random.randrange(0, self.environment.n_rules)
        self.converged = False
        # Populate agents
        self.agents = []
        for i in range(many_agents):
            self.agents.append(Agent(i, self.id, self.rule_set, many_objects, environment))

    def communicateFirstStage(self, ):
        # Get a random agent from the community as the speaker
        id_speaker = random.randrange(0, len(self.agents))

        # Select Random hearer from the remaining agents
        id_hearer = random.randrange(0, len(self.agents))
        while (id_hearer == id_speaker):
            id_hearer = random.randrange(0, len(self.agents))

        # Call communicateFirstStage function
        self.agents[id_speaker].communicateFirstStage(id_hearer)

    def communicateAmbassadors(self, id_community):
        for i in range(len(self.agents[0].objects)):
            self.environment.currentTime += 1
            self.agents[0].ambassadorCommunication(i, id_community)
            self.environment.saveCurrentStats()
    
    def saveFrequencies(self, id_community):
        for i in range(len(self.agents[0].objects)):
            self.environment.currentTime += 1
            self.agents[0].saveFrequencies(i, id_community)
            self.environment.saveCurrentStats()
    
    def purgeLessFrequentWords(self, ):
        for i in range(len(self.agents[0].objects)):
            self.environment.currentTime += 1
            self.agents[0].purgeLessFrequentWords(i)
            self.environment.saveCurrentStats()

    def propagateWordList(self, ):
        for i in range(1,len(self.agents)):
            for j in range(len(self.agents[0].objects)):
                self.environment.currentTime += 1
                self.agents[i].objects[j] = self.agents[0].objects[j]
                self.environment.saveCurrentStats()
                
