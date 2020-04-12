import numpy as np
import networkx as nx
import pylab
import time
import matplotlib.pyplot as plt
import random as rd
import gurobipy as grb
from itertools import permutations as PERM
from itertools import combinations as COMB
'''
L = 2
#R = int(a.max(0)[2])
R=16
#x = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
t1=(3.665,4.943,10.843,15.572,29.894,44.397,78.611,92.771,304.288,204.437,438.215,1393.307,1978.540,2144.440,4258.804)
t2=(3.603,4.941,10.819,15.549,29.592,43.889,73.822,88.176,240.562,175.666,310.668,770.088,962.023,1089.090,1564.475)
t3=(127.068,117.132,129.490,121.139,130.946,122.012,115.395,120.962,139.284,122.473,122.430,134.358,144.216,121.641,120.574)
v1=(0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000,0.0000000000)
v2=(0.1842137493,0.1567850946,0.1317888355,0.1183990724,0.1127521878,0.0833087759,0.0803031620,0.094040522,0.0546513741,0.0682078685,0.0560690074,0.0475832748,0.0464779408,0.0553075488,0.0542943312)
x=np.array((3,4,5,6,7,8,9,10,11,12,13,14,15,16,17))
t1=np.array(t1)
t2=np.array(t2)
t3=np.array(t3)
v1=np.array(v1)
v2=np.array(v2)
'''




'''
t1 = np.zeros(R-L+1)
a = np.loadtxt('../specase.out')
#a = np.loadtxt('/Users/apple/Desktop/hta/Courses/CMU/ridesharing/Dp/Ridesharing/Ridesharing/Exp2.txt')
N=a.shape[0]
print(a)
for i in range(N):
    if int(a[i][0])>R:
        continue;
    t1[int(a[i][0])-L]+=a[i][1]/5
print(t1)

t2 = np.zeros(11-L+1)
a = np.loadtxt('../specase2.out')
#a = np.loadtxt('/Users/apple/Desktop/hta/Courses/CMU/ridesharing/Dp/Ridesharing/Ridesharing/Exp2.txt')
N=a.shape[0]
for i in range(N):
    if int(a[i][0])>R:
        continue;
    t2[int(a[i][0])-L]+=a[i][1]/5

'''

def printTime():
    #baseLineTime=[2.84E+06,41519.6,44626,4363.5,388222,45424.6,6341.39,4765.26,691499,13924.7,1.05E+06,20267.8,1.60E+06,409944,158413,35390.8,154196,12865.3,5349.39,56537.3,284846,8206.23,4848.24,5587.22,71859.4,75369.3,610170,26294.1,5889.12,6822.64] //large 100
    #baseLineTime=[9304.11,7894.35,18.748,90.174,5437.8,11284.8,125695,93115.2,5017.36,273.566,1506.62,3174.34,9061.15,1937.08,337.515,495680,54834.8,19489,292.686,72983,2758.72,4427.49,445.191,2141.73,151.807,186321,66.271,365253,650.717,886.678,1567.04,25859.9,100.65,3589.84]#baseline 17
    #baseLineTime=[x/5*6 for x in [8465.39,1860.47,198490,27.594,18015.4,183742,285.308,82778.7,1459.97,5791.5,137.575,35121.1,445010,123.817,1072.62,491433,214.409,529.386,44.75,5310.33,86.088,368.619,8343.39,11376.4,125.623,4460.5,2599.08,1560.36]]#baseline 18
    #baseLineTime=[4636.47,1942.73,74144.7,433591,13992.1,293.152,211599,111788,160785,14985.3,134839,6717.15,38365,30915.4,716.57,649.771,8440.97,14012.6,11868.1,1554.53,15134.5,1731.04,90062,182566,1359.22,42435.6,58916.6]#basline 19
    #baseLineTime=[22470,3967.6,238944,151157,1113.21,92794.5,2159.76,191772,37149.7,4801.44,514.887,336249,1740.12,4912.58,2780.73,257352,27118.3,90343.1,2955.81,26571.2,60995.9,1255.76,6822.27,425.406,631.248,1763.95,30821,52712.8,3356.61]#baseline 20
    #baseLineTime=[111106,47918,88676.9,6102.82,972.569,114010,2397,244385,17712.5,10529,662.396,29771.1,144421,4880.46,1366.52,464.457,1027.7,358177,56382.4,747.643]#baseline22
    baseLineTime=[35277.5,10936.8,1945.63,110957,45670.6,11087.9,74511.2,324297,1211.22,6469.64,244115,49132.8,57345.7,14697.6,359.67]#baseline 24
    
    
    MLTime=[274307,53943.3,12494.1,2921.43,185217,53000.4,7454.41,64627.8,69208.1,1065.3,1620,84841.4,53885.6,20026.2,6081.76,381.396]#baseline24
    #MLTime=[149361,64245.3,179131,3441.96,1445.87,16354.8,4386.11,302581,14924.7,8418.35,1172.62,19414.8,26850.3,5160.64,1032.86,194637,297.626,1025.7,421781,36729.7,729.394]#baselien 22 #MLTime=[24092.8,1585.77,131266,82472.7,9123.25,18045,2156.8,183609,11126.8,4030.92,225.335,216533,3396.82,3558.23,4182.89,194673,2671.79,95018.5,2823.76,11091.3,48222.2,2389.52,2381.21,382.424,608.818,1766.69,22835.5,95527.2,3554.48]#ML 20
    #MLTime=[4590.25,2000.49,3211,375761,14796,276.214,256732,114308,88422.4,13855,13790,1636.14,39509.1,31429.6,1942.14,745.491,7434.21,20378.9,4708.69,3413.28,25106.8,1856.07,87484.4,160397,1049.01,22492.5,45784.3]#ML 19
    #MLTime=[x/5*6 for x in [6967.76,2238.8,64726.5,38.084,30030.2,182872,289.244,71313.4,1573.48,4906.55,119.272,29839.8,287728,141.888,1257.24,627.875,653.156,53.759,6360.69,98.661,405.879,27546.3,2198.94,7503.79,121.904,3840.54,2429.13,755.664]]#baseline 18
    #MLTime=[5830.96,7258.88,19.895,94.446,6577.26,11472.9,314005,92578.1,5311.35,286.445,1317.16,2933.64,4497.53,2021.01,337.731,249910,46195.8,15871.5,295.373,73247.7,1152.87,2423.21,449.792,2386.47,95.525,20245.2,67.273,285724,170171,646.006,1841.83,1594.52,25490.6,82.886,3557.57]#baseline 17
    #MLTime=[1.46E+06,28518.8,25868.2,3120.75,233853,28894,4496.76,4636.56,418536,8190.78,643550,13684.5,1.27E+06,798891,115100,25816.7,97040.4,9283.49,3931.74,40503.2,495968,5757.38,3528.06,3859.51,44352,383391,32363.4,433088,21077,4915.92,6397.28,2.59E+06]/large 100
    MLTime.sort()
    MLTime=[x/1000/60 for x in MLTime]
    print(MLTime)
    MLTimeY=[i+1 for i in range(len(MLTime))]
    MLTime.append(10)
    MLTimeY.append(len(MLTime)-1)

    baseLineTime.sort()
    baseLineTime=[x/1000/60 for x in baseLineTime]
    baseLineTimeY=[i+1 for i in range(len(baseLineTime))]
    baseLineTime.append(10)
    baseLineTimeY.append(len(baseLineTime)-1)

    print(len(MLTime))
    print(len(baseLineTime))
    
    FTsize=20
    NBsize=15
    LBsize=25
    plt.figure(figsize=(8,7))

    #x=np.array((0,10,20,30,40,50,60))
    x=np.array((0,2,4,6,8,10))
    #t1=np.array((25.13953488/60,315.75/60,1245/60,2701.875/60))

    plt.plot(baseLineTime,baseLineTimeY,'go-',mew=1,linewidth=1,label="BaseLine")
    #plt.errorbar(x,t1,yerr=te1/3,fmt='o',ecolor='g',color='g',elinewidth=2,capsize=4,alpha=0.5)

    plt.plot(MLTime,MLTimeY,'y*-',mew=1,linewidth=1,label="ML-guided")
    #plt.errorbar(x-0.1,t2,yerr=te2/3,fmt='*',ecolor='y',color='y',elinewidth=2,capsize=4)

    #plt.plot(x,t3,'r+-',mew=1,linewidth=1,label="T-Sampling")
    #plt.errorbar(x,t3,yerr=te3/3,fmt='+',ecolor='r',color='r',elinewidth=2,capsize=4)

    #plt.plot(x,t4,'b^-',mew=1,linewidth=1,label="GSA")
    #plt.errorbar(x+0.1,t4,yerr=te4/3,fmt='^',ecolor='b',color='b',elinewidth=2,capsize=4)


    plt.xticks(x,fontsize=NBsize)
    plt.yticks(fontsize=NBsize)
    plt.legend(fontsize=FTsize,bbox_to_anchor=(0.6,0.4))
    plt.xlabel("Time",fontsize=LBsize)
    plt.ylabel("Solved Instances",fontsize=LBsize)
    plt.savefig("dense22_Time.png")
    plt.show()
    



def printNode():
    #MLNode=[13049,255,230,32,2544,335,39,28,4913,54,7908,129,11967,8616,1329,313,1072,51,41,263,587,47,32,34,416,3582,383,4629,231,37,53,26540]#large100
    #MLNode=[419,144,6,8,392,326,551,1943,305,45,337,290,236,71,13,19871,3417,909,22,12770,205,466,19,584,26,284,8,9935,2977,17,356,147,222,13,46]#dense 17
    #MLNode=[106,835,6248,9,4539,8015,81,3174,410,148,21,7058,4043,34,74,83,38,8,409,11,30,3052,156,663,21,896,165,138]#dense 18
    #MLNode=[701,160,496,6637,978,40,74383,12298,5773,1581,904,195,4099,3376,419,27,1600,2858,666,501,4524,190,633,29792,79,1503,10963]#dense 19
    #MLNode=[3566,348,13630,1590,209,1038,521,7575,2742,360,60,29908,855,1104,1226,33216,628,16819,162,1322,6404,498,379,123,57,57,5170,2442,608]#dense 20
    #MLNode=[6332,10736,19769,556,232,2495,1029,48959,2684,863,224,2847,3700,342,148,31193,65,29,78523,2598,81]#dense 22
    MLNode=[69527,8247,3033,716,23653,6918,1477,12297,3265,238,282,12435,12573,1868,1659,28]#dense24
    #baseLineNode=[21137,347,341,33,2544,334,39,28,4961,54,7908,129,10903,3861,1327,313,1072,51,41,263,431,47,32,34,415,835,4629,231,37,53]#large 100
    #baseLineNode=[1103,144,6,8,380,327,475,1951,305,42,438,519,684,58,13,17678,3685,2054,22,14768,854,943,19,647,50,2653,8,10985,17,246,147,238,15,63]#dense17
    #baseLineNode=[94,981,34336,10,2820,10494,122,6515,409,186,29,9528,6795,32,72,17333,40,37,8,360,11,33,192,647,30,1434,173,404]#dense 18
    #baseLineNode=[908,243,12726,7643,808,47,75776,10433,17459,2919,33798,1969,4163,3297,131,22,1778,1887,1269,143,4366,208,683,60289,135,6448,24794]#dense 19
    #baseLineNode=[3451,1363,43290,2102,39,10590,474,7715,12547,699,212,82749,639,2010,869,62853,9482,25362,223,4112,9946,535,1928,175,50,61,5701,2177,595]#dense 20
    #baseLineNode=[5493,12792,17260,1455,179,38934,792,49743,5080,2545,215,7250,18343,460,165,133,29,77118,8461,77]#dense 22
    baseLineNode=[8171,3759,692,33965,15296,2316,21287,21351,325,2036,54466,12551,13798,5740,26]#dense 24
    MLNode.sort()
    MLNode=[x for x in MLNode]
    print(MLNode)
    MLNodeY=[i+1 for i in range(len(MLNode))]
    #MLNode.append(77118)
    #MLNodeY.append(len(MLNode)-1)
    #MLTime.append(60)
    #MLTimeY.append(len(MLTime)-1)

    baseLineNode.sort()
    baseLineNode=[x for x in baseLineNode]
    baseLineNodeY=[i+1 for i in range(len(baseLineNode))]
    baseLineNode.append(69527)
    baseLineNodeY.append(len(baseLineNode)-1)


    FTsize=20
    NBsize=15
    LBsize=25
    plt.figure(figsize=(8,7))

    #x=np.array((0,4500,9000,13500,18000,22500,27000))#large 100
    #x=np.array((0,15000,30000,45000,60000,75000))#dense17
    x=np.array((0,14000,28000,42000,56000,70000))#dense 20
    #t1=np.array((25.13953488/60,315.75/60,1245/60,2701.875/60))

    plt.plot(baseLineNode,baseLineNodeY,'go-',mew=1,linewidth=1,label="BaseLine")
    #plt.errorbar(x,t1,yerr=te1/3,fmt='o',ecolor='g',color='g',elinewidth=2,capsize=4,alpha=0.5)

    plt.plot(MLNode,MLNodeY,'y*-',mew=1,linewidth=1,label="ML-guided")
    #plt.errorbar(x-0.1,t2,yerr=te2/3,fmt='*',ecolor='y',color='y',elinewidth=2,capsize=4)

    #plt.plot(x,t3,'r+-',mew=1,linewidth=1,label="T-Sampling")
    #plt.errorbar(x,t3,yerr=te3/3,fmt='+',ecolor='r',color='r',elinewidth=2,capsize=4)

    #plt.plot(x,t4,'b^-',mew=1,linewidth=1,label="GSA")
    #plt.errorbar(x+0.1,t4,yerr=te4/3,fmt='^',ecolor='b',color='b',elinewidth=2,capsize=4)


    plt.xticks(x,fontsize=NBsize)
    plt.yticks(fontsize=NBsize)
    plt.legend(fontsize=FTsize,bbox_to_anchor=(0.6,0.4))
    plt.xlabel("Tree Size",fontsize=LBsize)
    plt.ylabel("Solved Instances",fontsize=LBsize)
    plt.savefig("dense24_Node.png")
    plt.show()
    


def printA(BL,ML,name,Feat):
    FTsize=20
    NBsize=15
    LBsize=25
    plt.figure(figsize=(8,7))
    x=[i for i in range(17,25)]
    x=np.array(x)
    #x=np.array((0,4500,9000,13500,18000,22500,27000))#large 100
    #x=np.array((0,15000,30000,45000,60000,75000))#dense17
    #x=np.array((0,14000,28000,42000,56000,70000))#dense 20
    #t1=np.array((25.13953488/60,315.75/60,1245/60,2701.875/60))

    plt.plot(x,BL,'go-',mew=1,linewidth=1,label="BaseLine")
    #plt.errorbar(x,t1,yerr=te1/3,fmt='o',ecolor='g',color='g',elinewidth=2,capsize=4,alpha=0.5)

    plt.plot(x,ML,'y*-',mew=1,linewidth=1,label="ML-guided")
    #plt.errorbar(x-0.1,t2,yerr=te2/3,fmt='*',ecolor='y',color='y',elinewidth=2,capsize=4)

    #plt.plot(x,t3,'r+-',mew=1,linewidth=1,label="T-Sampling")
    #plt.errorbar(x,t3,yerr=te3/3,fmt='+',ecolor='r',color='r',elinewidth=2,capsize=4)

    #plt.plot(x,t4,'b^-',mew=1,linewidth=1,label="GSA")
    #plt.errorbar(x+0.1,t4,yerr=te4/3,fmt='^',ecolor='b',color='b',elinewidth=2,capsize=4)


    plt.xticks(x,fontsize=NBsize)
    plt.yticks(fontsize=NBsize)
    #plt.legend(fontsize=FTsize,bbox_to_anchor=(0.6,0.4))
    plt.xlabel("#Agents",fontsize=LBsize)
    plt.ylabel(Feat,fontsize=LBsize)
    plt.savefig(name+".png")
    plt.show()

def plotdiffbar(x):
    FTsize=20
    NBsize=15
    LBsize=25
    fig=plt.figure(figsize=(8,7))
    #ax = fig.add_axes([0,0,1,1])
    langs = [i for i in range(17,25)]
    plt.bar(langs,x)
    plt.xticks(langs,fontsize=NBsize)
    plt.yticks(fontsize=NBsize)
    #plt.legend(fontsize=FTsize,bbox_to_anchor=(0.6,0.4))
    plt.xlabel("#Agents",fontsize=LBsize)
    plt.ylabel("Lowerbound Differences",fontsize=LBsize)
    plt.plot([16,25],[0,0],linewidth=0.5,color='black')
    plt.savefig("diff"+".png")
    #plt.set_title()
    plt.show()

Baselinediff=[0.1,0.075,0.1,0,0.1,-0.025,0.18,0.375]
plotdiffbar(Baselinediff)
exit()

BaselineTime=[1.01,1.15,1.02,0.95,1.48,1.46,1.91,1.65]
MLTime=[0.64,0.71,0.83,0.67,0.96,1.15,0.51,0.93]
printA(BaselineTime,MLTime,"runtime","Runtime/min")

BaselineSize=[1958,5544,10160,10067,21753,18284,26048,25815]
MLSize=[1639,2352,6125,4573,9228,10162,5479,9888]
#printA(BaselineSize,MLSize,"Treesize","Treesize")

BaselineRate=[85,70,67.5,72.5,65,50,37.5,37.5]
MLRate=[87.5,70,67.5,72.5,67.5,52.5,42.5,40]
printA(BaselineRate,MLRate,"SuccesRate","Success Rate/%")



exit()

printNode()

printTime()


exit()



plt.figure(figsize=(8,7))

gap=np.array((0,0.07,0.63,2.68))
plt.plot(x,gap,'go-',mew=1,linewidth=1,label="MILP")
#plt.errorbar(x-0.05,v2,yerr=ve2/3,fmt='*',ecolor='y',color='y',elinewidth=2,capsize=4)




plt.xticks(x,fontsize=NBsize)
plt.yticks(fontsize=NBsize)
plt.legend(fontsize=FTsize)
plt.xlabel("Number of Edges",fontsize=LBsize)
plt.ylabel("Optimality Gap/ x$10^{-3}$",fontsize=LBsize)
#plt.gca().set_yticklabels(['{:.1f}%'.format(x) for x in plt.gca().get_yticks()])

#plt.show()
plt.savefig("GapMILP.png")

plt.figure(figsize=(8,7))

rate=np.array((1,0.975,0.825,0.425))
plt.plot(x,rate,'go-',mew=1,linewidth=1,label="MILP")
#plt.errorbar(x-0.05,v2,yerr=ve2/3,fmt='*',ecolor='y',color='y',elinewidth=2,capsize=4)




plt.xticks(x,fontsize=NBsize)
plt.yticks(fontsize=NBsize)
plt.legend(fontsize=FTsize)
plt.xlabel("Number of Edges",fontsize=LBsize)
plt.ylabel("Optimality Rate (Cutoff Time = 1h)",fontsize=LBsize)
#plt.gca().set_yticklabels(['{:.1f}%'.format(x) for x in plt.gca().get_yticks()])

#plt.show()
plt.savefig("RateMILP.png")


'''
plt.figure(figsize=(8,7))
plt.plot(x,PNASv,'go-',mew=0.1,linewidth=1,label="RTV")
plt.plot(x,Greedyv,'r+-',mew=1,linewidth=1,label="Seq-MILP")
plt.plot(x,DPv,'b^-',mew=0.1,linewidth=1,label="Seq-DP")
plt.plot(np.linspace(10,30,30-10+1,dtype=int),OPTv,'y*-',mew=1,linewidth=1,label="OPT")
#plt.plot(x,PNASv,'go-',x,Greedyv,,x,DPv,'b^-')
plt.xticks(fontsize=NBsize)
plt.yticks(fontsize=NBsize)
plt.legend(fontsize=FTsize)
plt.xlabel("Requests",fontsize=LBsize)
plt.ylabel("Objective Value",fontsize=LBsize)
#plt.show()
plt.savefig("vmulti.png")

plt.figure(figsize=(8,7))
plt.plot(x,PNASr,'go-',mew=0.1,linewidth=1,label="RTV")
plt.plot(x,Greedyr,'r+-',mew=1,linewidth=1,label="Seq-MILP")
plt.plot(x,DPr,'b^-',mew=0.1,linewidth=1,label="Seq-DP")
plt.plot(np.linspace(10,30,30-10+1,dtype=int),OPTr,'y*-',mew=1,linewidth=1,label="OPT")
plt.xticks(fontsize=NBsize)
plt.yticks(fontsize=NBsize)
plt.legend(fontsize=FTsize)
plt.xlabel("Requests",fontsize=LBsize)
plt.ylabel("Satisfied Requests",fontsize=LBsize)
plt.savefig("rmulti.png")
plt.show()
'''

