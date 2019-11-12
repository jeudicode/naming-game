from pandas import DataFrame 

class DataExporter():

    def __init__(self, ):
        return

    def saveStatsObjectToCSV(self, O, N, C, i, statsObject):
        df = DataFrame.from_records([statsObject])
        filename = "./STATS/{}{}{}.csv".format(O,N,C)
        if (i == 0):
            df.to_csv (filename, index = None, header=True)
        else:
            df.to_csv(filename, index= None, mode='a', header=False)

