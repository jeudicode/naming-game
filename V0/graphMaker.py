import pandas as pd
import matplotlib.pyplot as plt

class graphMaker:

    def makeTimeGraph(self, filepath):
        data = []
        maxTime = 0
        for i in range(100):
            suffix = "_{}.csv".format(i)
            data.append(pd.read_csv(filepath + suffix))
            currentLen = len(data[i])
            if currentLen > maxTime:
                maxTime = currentLen
        
        totales = []
        for j in range(maxTime):
            total = 0.0
            for i in range(100):
                currentLen = len(data[i])
                if currentLen <= j:
                    row = data[i].iloc[currentLen - 1]
                else:
                    row = data[i].iloc[j]
                total += int(row["currentNumberOfDifferentWords"])
            total/=100.0
            totales.append(total)
        plt.plot(totales)
        plt.xlabel('Time')
        plt.ylabel('Total Words')
        plt.show()
        print(len(totales))


gr = graphMaker()
gr.makeTimeGraph("../STATS/333/333")