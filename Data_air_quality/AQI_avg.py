# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:09:32 2020

@author: Omkaar
"""

import pandas as pd
import os
import numpy as np
import time
import matplotlib.pyplot as plt


"""
The below functions are based on Krish Naik's AQI ML project.
"""

def avg_aqi_2013():
    
    temp_i=0
    average=[]
    
    for rows in pd.read_csv('E:/Python_Learning/ML/Data_air_quality/AQI/aqi2013.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is  str:
                if i!='NoData' and i!='PwrFail' and i!='...' and i!='Invld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average

def avg_aqi_2014():
    
    temp_i=0
    average=[]
    
    for rows in pd.read_csv('E:/Python_Learning/ML/Data_air_quality/AQI/aqi2014.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is  str:
                if i!='NoData' and i!='PwrFail' and i!='...' and i!='Invld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average

def avg_aqi_2015():
    
    temp_i=0
    average=[]
    
    for rows in pd.read_csv('E:/Python_Learning/ML/Data_air_quality/AQI/aqi2015.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is  str:
                if i!='NoData' and i!='PwrFail' and i!='...' and i!='Invld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average

def avg_aqi_2016():
    
    temp_i=0
    average=[]
    
    for rows in pd.read_csv('E:/Python_Learning/ML/Data_air_quality/AQI/aqi2016.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is  str:
                if i!='NoData' and i!='PwrFail' and i!='...' and i!='Invld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average

def avg_aqi_2017():
    
    temp_i=0
    average=[]
    
    for rows in pd.read_csv('E:/Python_Learning/ML/Data_air_quality/AQI/aqi2017.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is  str:
                if i!='NoData' and i!='PwrFail' and i!='...' and i!='Invld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average

def avg_aqi_2018():
    
    temp_i=0
    average=[]
    
    for rows in pd.read_csv('E:/Python_Learning/ML/Data_air_quality/AQI/aqi2018.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is  str:
                if i!='NoData' and i!='PwrFail' and i!='...' and i!='Invld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average

"""
I tried generalising the code above in one function itself.

"""

def avg_aqi_years():
    
    temp_i=0
    average_2013=[]
    average_2014=[]
    average_2015=[]
    average_2016=[]
    average_2017=[]
    average_2018=[]
    
    for years in range(2013,2019):
        for rows in pd.read_csv('E:/Python_Learning/ML/Data_air_quality/AQI/aqi{}.csv'.format(years),chunksize=24):
            add_var=0
            avg=0.0
            data=[]
            df=pd.DataFrame(data=rows)
            for index,row in df.iterrows():
                data.append(row['PM2.5'])
            for i in data:
                if type(i) is float or type(i) is int:
                    add_var+=i
                elif type(i) is  str:
                    if i!='NoData' and i!='PwrFail' and i!='...' and i!='Invld' and i!='---' and i!='InVld':
                        temp=float(i)
                        add_var+=temp
            avg=add_var/24
            temp_i+=1
            if years==2013:
                average_2013.append(avg)
            elif years==2014:
                average_2014.append(avg)
            elif years==2015:
                average_2015.append(avg)
            elif years==2016:
                average_2016.append(avg)
            elif years==2017:
                average_2017.append(avg)
            elif years==2018:
                average_2018.append(avg)
        #average.append(year_list[years])
    return average_2013,average_2014,average_2015,average_2016,average_2017,average_2018

        
        

if __name__=="__main__":
    
    list_of_average=[]
    list_of_average=avg_aqi_years()
    print(list_of_average)
    for i in range(len(list_of_average)):
        plt.plot(range(len(list_of_average[i])),list_of_average[i],label="data")