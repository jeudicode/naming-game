from Agent import Agent
import random
import string 

class Community():

    def __init__(self, id, rule_set, many_objects, many_agents, environment):
        self.environment = environment
        self.id = id
        self.rule_set = rule_set
        self.converged = False
        # Populate agents
        self.agents = []
        for i in range(many_agents):
            self.agents.append(Agent(i, rule_set, many_objects, environment))

    def communicateFirstStage(self, ):
        # Get a random agent from the community as the speaker
        id_speaker = random.randrange(0, len(self.agents))

        # Select Random hearer from the remaining agents
        id_hearer = random.randrange(0, len(self.agents))
        while (id_hearer == id_speaker):
            id_hearer = random.randrange(0, len(self.agents))

        # Call communicateFirstStage function
        self.agents[id_speaker].communicateFirstStage(id_hearer)
