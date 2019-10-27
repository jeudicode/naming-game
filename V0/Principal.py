from Environment import Environment

# We create a new environment with 10 objects, 50 agents per community and 4 communities
env = Environment(10, 50, 4)
env.communicateFirstStage()