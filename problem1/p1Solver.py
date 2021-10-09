from problem1.asiaNet import AsiaNet
import numpy as np

class P1Solver:

    def __init__(self, asiaNet: AsiaNet):
        # import data
        self.cost = asiaNet.cost
        self.time = asiaNet.time
        self.num = asiaNet.num_nodes
        self.T = 10

        # initialize the d and p
        self.d = np.empty([self.num,self.T])
        self.p = np.empty([self.num,self.T])
        for i in range(self.num):
            for j in range(self.T):
                self.d[i][j] = np.nan
                self.p[i][j] = np.nan
        self.d[3][0] = 0





    def solve(self):
        for k in range(self.T):
            for j in range(self.num):
                for i in range(self.num):
                    if not np.isnan(self.cost[i][j]):
                        ksubtij = int(k - self.time[i][j])
                        #print(str(ksubtij))

                        if ksubtij >= 0 :
                            if not np.isnan(self.d[i][ksubtij]):
                                #print('go1')

                                if np.isnan(self.d[i][j]):
                                    #print('go2')
                                    self.d[j][k] = self.d[i][ksubtij] + self.cost[i][j]
                                    self.p[j][k] = i
                                else:
                                    if(self.d[i][ksubtij] + self.cost[i][j]< self.d[i][j]):
                                        #print('go3')
                                        self.d[j][k] = self.d[i][ksubtij] + self.cost[i][j]
                                        self.p[j][k] = i
        print(self.d)
        print(self.p)





