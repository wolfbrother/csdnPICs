# -*- coding: cp936 -*-
import numpy
import random

import matplotlib.pyplot as pyplot



def add(x):
    temp=[]
    for i in range(x.shape[0]):
        a=x[i].tolist() 
        a.append(1)     #append����������������ƻ���ԭ���Ľṹ���������ض���
        temp.append(a)
    x=numpy.array(temp)
    return x
def Gram(x):
    G=numpy.zeros([x.shape[0],x.shape[0]])
    for i in range(x.shape[0]):
        for j in range(i+1):
            G[i][j]=G[j][i]=x[i].dot(x[j])
    return G       

def Main():
    x=numpy.array([[3,3],[4,3],[1,1],[2,1]])
    y=numpy.array([1,1,-1,-1])
    x=add(x)
    G=Gram(x)
    alpha=numpy.zeros([1,x.shape[0]])
    eta=0.31415
    indic=alpha*y.dot(G)*y
    errorset=[]
    for i in range(indic.shape[1]):
        if indic[0][i]<=0:
            errorset.append(i)
    while len(errorset)>0:
        num=random.randrange(0,len(errorset))
        i=errorset[num]
        alpha=alpha+eta*y[i]*y*G[i]
        print alpha
        indic=alpha*y.dot(G)*y
        errorset=[]
        for i in range(indic.shape[1]):
            if indic[0][i]<=0:
                errorset.append(i)          
    print (alpha*y).dot(x)# Ҫ������������
Main()
 


        
    

