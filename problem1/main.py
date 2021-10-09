import csv
from problem1.asiaNet import AsiaNet
from constants import PATH
from problem1.p1Solver import P1Solver
import numpy as np

if __name__ == '__main__':
    ## read cost/time data from files
    ## -1 represents null TO BE CONVERTED TO np.nan later
    costPath = PATH + '/data/asiaNetRed.csv'
    timePath = PATH + '/data/asiaNetGreen.csv'
    costFile = open(costPath)
    timeFile = open(timePath)
    costReader = csv.reader(costFile,quoting=csv.QUOTE_NONNUMERIC)
    timeReader = csv.reader(timeFile,quoting=csv.QUOTE_NONNUMERIC)
    cost = []
    for row in costReader:
        cost.append(row)
    time = []
    for row in timeReader:
        time.append(row)
    costFile.close()
    timeFile.close()
    # covert null in cost/time from -1 to np.nan
    cost = np.array(cost)
    time = np.array(time)
    for i in range(len(cost)):
        for j in range(len(cost)):
            if (time[i][j] == -1):
                time[i][j] = np.nan
            if (cost[i][j] == -1):
                cost[i][j] = np.nan

    ## problem instance
    asiaNet = AsiaNet(cost,time)

    ## solver instance
    solver = P1Solver(asiaNet)
    solver.solve()
