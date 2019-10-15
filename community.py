from agent import Agent

class Community:

    members = []
    ruleset = 0

    def __init__(self, members, ruleset, number_of_objects):
        self.ruleset = ruleset
        for i in range(members):
            self.members.append(Agent(number_of_objects, ruleset))


    def getMembers(self):
        return self.members