from Environment import Environment
from DataExporter import DataExporter

# Data exporter
dexpr = DataExporter()

# Experiment Values
O_values = [4, 8, 16]
N_values = [50, 100, 200]
C_values = [4, 8, 16]

# We create a new environment with objects, agents per community and communities
for i in range(3):
    for j in range(3):
        for k in range(3):        
            for l in range(100):
                env = Environment(O_values[i], N_values[j], C_values[k])
                env.communicateFirstStage()
                env.communicateSecondStage()
                dexpr.saveStatsObjectToCSV(i + 1, j + 1, k + 1, l, env.archive_stats)