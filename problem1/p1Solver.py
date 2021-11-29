from problem1.asiaNet import AsiaNet
import numpy as np

class P1Solver:

    def __init__(self, asiaNet: AsiaNet):
        # import data
        self.cost = asiaNet.cost
        self.time = asiaNet.time
        self.num = asiaNet.num_nodes
        self.T = 11

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

    def postAnalysis(self):
        opt = []
        #print(len(self.d))
        #print(len(self.d[0]))
        for i in range(len(self.d)):
            opt.append([])
            for j in range(len(self.d[0])):
                if not np.isnan(self.d[i][j]):
                    if len(opt[i]) == 0:
                        opt[i].append(j)
                    else:
                        index = opt[i][-1]
                        if self.d[i][j] < self.d[i][index]:
                            opt[i].append(j)
        for i in range(len(opt)):
            for j in range(len(opt[i])):
                if opt[i][j] == 0:
                    print('Original Point:' + str(i))
                else:
                    index = opt[i][j]
                    objmsg = "End Point:"+ str(i)+ ", Optimal cost:" +str(self.d[i][index])+ ", Optimal time:"+str(index)
                    print(objmsg)
                    this = int(i)
                    next = int(self.p[i][index])
                    time = int(index)
                    pathmsg = "Optimal solution:" +str(this) +'<-' + str(next)
                    while(time > 0):
                        #print('this:'+str(this)+' next'+str(next))
                        #print('time left:' + str(time))
                        #print('time consumed:'+str(self.time[next][this]))
                        time -= int(self.time[next][this])
                        this = int(next)
                        #print('this:'+str(this)+'time:'+str(time))
                        if time > 0:
                            next = int(self.p[this][time])
                            pathmsg += '<-' + str(next)

                    print(pathmsg)






