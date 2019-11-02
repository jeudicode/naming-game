from Environment import Environment

# We create a new environment with 10 objects, 50 agents per community and 4 communities
env = Environment(16, 201, 7)
env.communicateFirstStage()
env.communicateSecondStage()