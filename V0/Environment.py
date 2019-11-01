from Community import Community
import random 

class Environment():
    
    def __init__(self, many_objects, many_agents_per_community, many_communities):
        # Save the stats
        self.archive_stats = []
        
        # Save current Time
        self.currentTime = 0

        # Save converged first stage flag
        self.converged_first_stage = False

        # Populate the Communities array
        self.communities = []
        for i in range(many_communities):
            # Set fixed rule set
            rule_set = i + 1
            self.communities.append(Community(i, rule_set, many_objects, many_agents_per_community, self))

        # Save and print the current Stats
        # self.saveCurrentStats()
        # self.printStats()

    def communicateFirstStage(self, ):
        while(True):
            self.currentTime += 1
            self.passTimeFirstStage()
            if (self.converged_first_stage == True):
                break
    
    def communicateSecondStage(self, ):
        self.communicateAmbassadors()
        self.saveFrequenciesAfterCommunication()
        print("Ended Second Stage!")
        for i in range(len(self.communities)):
            print("//////////////")
            print("--------------------")
            print(self.communities[i].agents[0].objects)
            print("--------------------")
            print("//////////////")

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
                self.currentTime += 1
                self.communities[i].saveFrequencies(j)
            self.communities[i].purgeLessFrequentWords()
            self.communities[i].propagateWordList()

    def passTimeFirstStage(self, ):
        self.makeCommunicationFirstStage()
        self.checkConvergedFirstStage()
        # self.saveCurrentStats()
        # self.printStats()
    
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
            print("Ended First Stage!")
            print("////////////////////")
            for i in range(len(self.communities)):
                print("--------------------")
                print(self.communities[i].agents[0].objects)
                print("--------------------")
            print("////////////////////")
            self.converged_first_stage = True

    # def saveCurrentStats(self, ):
        # currentState = {
        #     "currentNumberOfWords": 0,
        #     "maxNumberOfWords": 0,
        #     "currentTime": 0,
        #     "timeWithMaxWords": 0,
        #     "convergenceTime": -1,
        #     "maxNumberOfDifferentWords": 0,
        #     "currentNumberOfDifferentWords": 0
        # }

        # currentDifferentWords = set()
        # allAgentsHaveWords = True
        # for i in range(len(self.agents)):
        #     if (len(self.agents[i].words) == 0):
        #         allAgentsHaveWords = False 
        #     for j in range(len(self.agents[i].words)):
        #         currentDifferentWords.add(self.agents[i].words[j])
        #     currentState["currentNumberOfWords"] += len(self.agents[i].words)
        #     currentState["currentTime"] = self.currentTime

        # currentState["currentNumberOfDifferentWords"] = len(currentDifferentWords)

        # if (len(self.archive_stats) > 0):
        #     # Update maximum number of Words
        #     if (currentState["currentNumberOfWords"] > self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfWords"]):
        #         currentState["maxNumberOfWords"] = currentState["currentNumberOfWords"]
        #         currentState["timeWithMaxWords"] = self.currentTime
        #     else: 
        #         currentState["maxNumberOfWords"] = self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfWords"]
        #         currentState["timeWithMaxWords"] = self.archive_stats[len(self.archive_stats) - 1]["timeWithMaxWords"]

        #     # Update maximum number of different Words 
        #     if (currentState["currentNumberOfDifferentWords"] > self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfDifferentWords"]):
        #         currentState["maxNumberOfDifferentWords"] = currentState["currentNumberOfDifferentWords"]
        #     else: 
        #         currentState["maxNumberOfDifferentWords"] = self.archive_stats[len(self.archive_stats) - 1]["maxNumberOfDifferentWords"]
        
        # if (allAgentsHaveWords and len(currentDifferentWords) == 1):
        #     currentState["convergenceTime"] = self.currentTime
        #     self.converged_first_stage = True
        
        # self.archive_stats.append(currentState)

    # def printStats(self, ):
    #     print("======== Time: " + str(self.currentTime) + " ========")
    #     print(self.archive_stats[len(self.archive_stats) - 1])
