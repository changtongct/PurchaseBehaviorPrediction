# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:54:18 2016

@author: Administrator
"""

import csv

def SplitTime():
    read_user = csv.reader(file(r'tianchi_fresh_comp_train_user.csv', 'rb')) 
    writer = csv.writer(file('WashedData-simplified.csv', 'wb'))  
    i=0;
    for row in read_user:
        if i==0:
            writer.writerow(['user_id', 'item_id', 'behavior_type','month','day','hour']);
            i+=1;
        else:
            a=row[5].replace('-',' ');
            a=a.split();
            b=[(row[0]),(row[1]),(row[2]),(a[1]),(a[2]),(a[3])];
            writer.writerow(b);   


def ExtractDayXtoY(x,y):    # x and y belong to 1 to 31
    read_user = csv.reader(file(r'WashedData-simplified.csv', 'rb'))    
    writer = csv.writer(file('Day'+str(x)+'To'+str(y)+'.csv', 'wb'))   
    firstday = 17+x;
    lastday = 17+y;
    month = 12;   
    i=0;
    for row in read_user:
        if i==0:
            writer.writerow(['user_id', 'item_id', 'behavior_type']);
            i+=1;
        else:
            temp=int(row[4]);
            if int(row[3])==month:
                temp+=30;
            if temp>=firstday and temp<=lastday:
                writer.writerow([(row[0]),(row[1]),(row[2])]);   
                
if __name__=="__main__":
#    SplitTime();
#    ExtractDayXtoY(1,3);
    ExtractDayXtoY(29,31);