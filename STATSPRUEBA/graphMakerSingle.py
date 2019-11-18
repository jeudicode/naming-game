import pandas as pd
import matplotlib.pyplot as plt

class graphMaker:

    def makeTimeGraph(self, objetos, agentes, comunidades, filepath):
        printData = {
            "convergenceTime": 0.0,
            "timeWithMaxWords": 0.0,
            "maxNumberOfWords": 0.0,
            "maxNumberOfDifferentWords": 0.0,
            "TConvOverTMax": 0.0,
        }
        for i in range(100):
            suffix = "_{}.csv".format(i)
            data = pd.read_csv(filepath + suffix)
            currentLen = len(data)
            row = data.iloc[currentLen - 1]
            printData["convergenceTime"] += float(row["convergenceTime"])    
            printData["timeWithMaxWords"] += float(row["timeWithMaxWords"])    
            printData["maxNumberOfWords"] += float(row["maxNumberOfWords"])    
            printData["maxNumberOfDifferentWords"] += float(row["maxNumberOfDifferentWords"])    
            if (int(row["timeWithMaxWords"]) != 0):
                printData["TConvOverTMax"] += float(row["convergenceTime"]) / float(row["timeWithMaxWords"])    
        printData["convergenceTime"] /= 100.0
        printData["timeWithMaxWords"] /= 100.0
        printData["maxNumberOfWords"] /= 100.0
        printData["maxNumberOfDifferentWords"] /= 100.0
        printData["TConvOverTMax"] /= 100.0
        print("-----------------------{}-{}-{}-------------------------------------".format(objetos, agentes, comunidades))
        print(printData)
        print("--------------------------------------------------------------------".format(objetos, agentes, comunidades))
        

# Tiempo de convergencia
# Tiempo con número maximo de palabras totales
# número máximo de palabras totales
# número máximo de palabras diferentes
# Tiempo de convergencia / tiempo máximo de palabras totales

# 4 50 4 | 1 1 1 
# 8 50 4 | 2 1 1
# 16 50 4 | 3 1 1

# 4 50 4 | 1 1 1
# 4 50 8 | 1 1 2
# 4 50 16 | 1 1 3

# 4 100 4 | 1 2 1
# 8 100 4 | 2 2 1
# 16 100 4 | 3 2 1

# 4 100 4 | 1 2 1
# 4 100 8 | 1 2 2
# 4 100 16 | 1 2 3

# 4 200 4 | 1 3 1
# 8 200 4 | 2 3 1
# 16 200 4 | 3 3 1

# 4 200 4 | 1 3 1
# 4 200 8 | 1 3 2
# 4 200 16 | 1 3 3

gr = graphMaker()
for i in range(3):
    filepath = "../STATS/"
    for j in range(3):
        filename = "{}{}{}/{}{}{}".format(j + 1, i + 1, 1, j + 1, i + 1, 1)
        gr.makeTimeGraph(j + 1, i + 1, 1,filepath + filename)
    for j in range(3):
        filename = "{}{}{}/{}{}{}".format(1, i + 1, j + 1, 1, i + 1, j + 1)
        gr.makeTimeGraph(1, i + 1, j + 1,filepath + filename)