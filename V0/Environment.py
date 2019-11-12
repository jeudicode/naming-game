from Community import Community
import random 

class Environment():
    
    def __init__(self, many_objects, many_agents, many_communities):
        # Save the stats
        self.archive_stats = []
        
        # Save current Time
        self.currentTime = 0

        # Set Current number of rule sets
        self.n_rules = 4

        # Save converged first stage flag
        self.converged_first_stage = False

        # Populate the Communities array
        self.communities = []
        many_agents_per_community = int(many_agents/many_communities)
        for i in range(many_communities):
            if i == (many_communities - 1):
                many_agents_per_community = many_agents
            many_agents = many_agents - many_agents_per_community
            self.communities.append(Community(i, many_objects, many_agents_per_community, self))

        # Save and print the current Stats
        self.saveCurrentStats()

    def communicateFirstStage(self, ):
        while(True):
            self.currentTime += 1
            self.saveCurrentStats()
            self.passTimeFirstStage()
            if (self.converged_first_stage == True):
                break
    
    def communicateSecondStage(self, ):
        self.communicateAmbassadors()
        self.saveFrequenciesAfterCommunication()
        # print("Ended Second Stage!")
        # for i in range(len(self.communities)):
        #     print("//////////////")
        #     print("--------------------")
        #     print(self.communities[i].agents[0].objects)
        #     print("--------------------")
        #     print("//////////////")
        # print(self.archive_stats[len(self.archive_stats) - 1])


    def communicateAmbassadors(self, ):
        for i in range(len(self.communities)):
            for j in range(len(self.communities)):
                if (i == j):
                    continue
                self.communities[i].communicateAmbassadors(j)
    
    def saveFrequenciesAfterCommunication(self ,):
        for i in range(len(self.communities)):
            for j in range(len(self.communities)):
                if (j == i):
                    continue
                self.communities[i].saveFrequencies(j)
            self.communities[i].purgeLessFrequentWords()
            self.communities[i].propagateWordList()

    def passTimeFirstStage(self, ):
        self.makeCommunicationFirstStage()
        self.checkConvergedFirstStage()
        
    def makeCommunicationFirstStage(self, ):
    
        # Select Random community
        id_community = random.randrange(0, len(self.communities))

        # Call communicate function in the community
        self.communities[id_community].communicateFirstStage()

    def checkConvergedFirstStage(self, ):
        all_communities_converged = True
        for i in range(len(self.communities)):
            converged = True
            for j in range(len(self.communities[i].agents)):
                only_one_word_per_object = True
                
                for k in range(len(self.communities[i].agents[j].objects)):
                    if (len(self.communities[i].agents[j].objects[k]) != 1):
                        only_one_word_per_object = False
                if (only_one_word_per_object == False):
                    converged = False
            if (converged == False):
                all_communities_converged = False
            else:
                self.communities[i].converged = True
            
        if (all_communities_converged == True):
            # print("Ended First Stage!")
            # print("////////////////////")
            # for i in range(len(self.communities)):
            #     print("--------------------")
            #     print(self.communities[i].agents[0].objects)
            #     print("--------------------")
            # print("////////////////////")
            self.converged_first_stage = True

    def saveCurrentStats(self, ):
        currentState = {
            "currentNumberOfWords": 0,
            "maxNumberOfWords": 0,
            "currentTime": 0,
            "timeWithMaxWords": 0,
            "convergenceTime": -1,
            "maxNumberOfDifferentWords": 0,
            "currentNumberOfDifferentWords": 0
        }

        currentDifferentWords = set()
        for i in range(len(self.communities)):
            for j in range(len(self.communities[i].agents)):
                for k in range(len(self.communities[i].agents[j].objects)):
                    for l in range(len(self.communities[i].agents[j].objects[k])):
                        currentDifferentWords.add(self.communities[i].agents[j].objects[k][l][1])
                    currentState["currentNumberOfWords"] += len(self.communities[i].agents[j].objects[k])
        
        currentState["currentTime"] = self.currentTime
        currentState["convergenceTime"] = self.currentTime
        currentState["currentNumberOfDifferentWords"] = len(currentDifferentWords)

        if (len(self.archive_stats) > 0):
            # Update maximum number of Words
            if (currentState["currentNumberOfWords"] > self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfWords"]):
                currentState["maxNumberOfWords"] = currentState["currentNumberOfWords"]
                currentState["timeWithMaxWords"] = self.currentTime
            else: 
                currentState["maxNumberOfWords"] = self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfWords"]
                currentState["timeWithMaxWords"] = self.archive_stats[len(self.archive_stats) - 1]["timeWithMaxWords"]

            # Update maximum number of different Words 
            if (currentState["currentNumberOfDifferentWords"] > self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfDifferentWords"]):
                currentState["maxNumberOfDifferentWords"] = currentState["currentNumberOfDifferentWords"]
            else: 
                currentState["maxNumberOfDifferentWords"] = self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfDifferentWords"]
        
        self.archive_stats.append(currentState)
