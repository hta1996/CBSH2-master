import gurobipy as grb
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import sample
import math
import random
import osmnx as ox
import shapefile
import csv
import fiona
import sys
import matplotlib.lines as mlines

filename="featureLarge100_"

def normalize(vv):
    t=vv
    for i in range(3,len(t[0])-1):
        M=0
        for s in t:
            if math.fabs(eval(s[i]))>M:
                M=math.fabs(eval(s[i]))
        if math.fabs(M)<1e-7: continue
        #print(M)
        for j in range(len(t)):
            
            v=eval(t[j][i])*1./M
            t[j][i]=str(v)
    return t

def relabel(data):
    score=[]
    datanew=[]
    for t in data:
        score.append(eval(t[2]))
    score.sort()
    tp=int(len(score)/10)
    tpj=tp+1
    while tpj<len(score):
        if score[tpj]!=score[tp]: break
        tpj+=1
    if tpj*1./len(score)>=0.2:
        tpk=tp
        while tp>0:
            if score[tpk]!=score[tp]: break
            tp-=1
    for t in data:
        s=t
        if eval(s[2])-1e-8<=score[tp]:
            s[0]="1"
        else:
            s[0]="0"
        datanew.append(s)
    return datanew

def printdata(t,count,f):
    for s in t:
        f.write(s[0]+" qid:"+str(count)+" ")
        ss=s[3:]
        for i in range(len(ss)-1):
            f.write(str(i+1)+":"+ss[i]+" ")
        f.write("\n")
        
data=[]
for i in range(10):
    datap=[]
    with open(filename+str(i)+".txt",'r') as f:
        for line in f:
            t=[x for x in line.split(' ')]
            if len(t)<2:
                #relabel(datap)
                data.append(datap)
                datap=[]
                continue
            datap.append(t)
    if len(datap)>0:
        #relabel(datap)
        data.append(datap)


L=2000
random.shuffle(data)
print(len(data))
traindata=data[:]
if len(data)>L:
    traindata=data[:L]
count=0

with open(filename+"train.txt",'w') as f:
    for i in traindata:
        count+=1
        tt=normalize(i)
        printdata(tt,count,f)


data=[]
for i in range(10,20):
    datap=[]
    with open(filename+str(i)+".txt",'r') as f:
        for line in f:
            t=[x for x in line.split(' ')]
            if len(t)<2:
                data.append(datap)
                datap=[]
                continue
            datap.append(t)
    if len(datap)>0:
        data.append(datap)




print(len(data))
testdata=data[:]
count=0


with open(filename+"test.txt",'w') as f:
    for i in testdata:
        count+=1
        tt=normalize(i)
        printdata(tt,count,f)

exit()


for i in range(10):
    datap=[]
    with open(filename+str(i)+".txt",'r') as f:
        for line in f:
            t=[x for x in line.split(' ')]
            if len(t)<2:
                data.append(datap)
                datap=[]
                continue
            datap.append(t)
    if len(datap)>0:
        data.append(datap)



splitFeat=int(len(data)*0.6)
random.shuffle(data)

print(len(data))

Ttest=1000;

if splitFeat>Ttest:
    splitFeat=Ttest

traindata=data[:splitFeat]
testdata=data[splitFeat:]

count=0


    
with open(filename+"train.txt",'w') as f:
    for i in traindata:
        count+=1
        printdata(i,count,f)

with open(filename+"test.txt",'w') as f:
    for i in testdata:
        count+=1
        printdata(i,count,f)

