from pandas import DataFrame 
import os

class DataExporter():

    def __init__(self, ):
        return

    def saveStatsObjectToCSV(self, O, N, C, iteracion, statsObjectArray):
        filepath = "./STATS/{}{}{}/".format(O,N,C)
        filename = "{}{}{}_{}.csv".format(O,N,C, iteracion)
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        for i in range(len(statsObjectArray)):
            df = DataFrame.from_records([statsObjectArray[i]])
            if (i == 0):
                df.to_csv (filepath + filename, index = None, header=True)
            else:
                df.to_csv(filepath + filename, index= None, mode='a', header=False)

