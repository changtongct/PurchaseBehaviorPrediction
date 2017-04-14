# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\star\.spyder2\.temp.py
"""
#import matplotlib.pyplot as plt
import pandas as pd
#from Plots import*
import csv

#read_user = csv.reader(file(r'Day1To3.csv', 'r'))

#a = read_user.groupby(['date','time'])['user_id'].count()
#a.plot(color='r',grid='on',title='Number of operations per hour');
#b = read_user.groupby('date')['user_id'].count()
#b.plot(color='r',grid='on',title='Number of operations per day');
#c = read_user.groupby('time')['user_id'].count()
#c.plot(color='r',grid='on',title='Average number of operations per hour');

def value(x):
    i=0;    
    for row in x:
        if row==1:
            i+=1;
        elif row==2:
            i+=3;
        elif row==3:
            i+=6;
        else:
            i=0;
    return i;

if __name__=="__main__":
    read_user = pd.read_csv('Day29To31.csv')
    d=read_user.groupby(['item_id','user_id'])['behavior_type'].agg(value); 
###############################################################################
#    result = csv.writer(file('result.csv', 'wb'))     
#    i=0; 
#    for xvalue in d:
#        if xvalue>2:
#            b = [(d.index[i][0]),(d.index[i][1])];
#            result.writerow(b);
#        i+=1;
    
#    result = []
#    i=0; 
#    temp = 0;
#    for xvalue in d:
#        if xvalue>2:
#            b = (d.index[i][0],d.index[i][1]);
#            if d.index[i][0]==temp:
#                continue;
#            else:
#                temp = d.index[i][0]
#            result.append(b);
#        i+=1;
    
    result = {}
    i=0; 
    for xvalue in d:
        if xvalue>2:
            result[d.index[i][0]] = d.index[i][1];
        i+=1;    
    ccc = pd.Series(result)
###############################################################################  
    read_item = pd.read_csv('tianchi_fresh_comp_train_item_new.csv');
    t = {}    
    for i in range(0,620917):
        t[read_item.ix[i]['item_id']] = 0;
    ddd = pd.Series(t)    
    ct = ccc+ddd
    ct1 = ct.dropna()
    
    final = csv.writer(file('tianchi_mobile_recommendation_predict.csv', 'wb'))   
    for i in range(0,22791):
        b = (str(int(ct1.values[i])), str(ct1.index[i]))
        final.writerow(b)

#    i=0;
#    temp=0;    
#    for row in read_item:
#        if i==0:
#            i+=1;
#        else:
#            for xindex in d.index:
#                xindex=temp;
#                if int(row[0])==xindex[0]:
#                    temp=xindex;
#                    b=[(row[0]),(xindex[0])];
#                    result.writerow(b);
#                    break;
        