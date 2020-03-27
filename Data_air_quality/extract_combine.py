# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:57:18 2020

@author: Omkaar
"""


from AQI_avg import avg_aqi_years
import requests
import sys
import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os
import csv



def meta_data(year,month):
    html_file=open('E:\Python_Learning\ML\Data_air_quality\{}\{}.html'.format(year,month),'rb')
    read_file=html_file.read()
    tempD=[]
    finalD=[]
    soup=BeautifulSoup(read_file,'lxml')
    
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a=tr.get_text()
                tempD.append(a)
    
    #index_row=tempD[:16]
    num_rows=len(tempD)/15
    
    for times in range(round(num_rows)):
        newtempD=[]
        
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
            
        finalD.append(newtempD)
        
    

    length_final=len(finalD)
    finalD.pop(length_final-1)
    finalD.pop(0)
    
    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)
    
    
        
    return finalD
                


def combine_data(year,cs):
    for a in pd.read_csv('E:\Python_Learning\ML\Data_air_quality\Real_Data\combined_' +str(year)+ '.csv',chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist=df.values.tolist()
    return mylist
        
        
                
if __name__=='__main__':
    
    total=[]
    
    if not os.path.exists('E:\Python_Learning\ML\Data_air_quality\Real_data'):
        os.makedirs('E:\Python_Learning\ML\Data_air_quality\Real_data')
    
    
    aqi_final_13,aqi_final_14,aqi_final_15,aqi_final_16,aqi_final_17,aqi_final_18=avg_aqi_years()
    
    for year in range(2013,2019):
        final_data=[]

        for month in range(1,13):
            temp=meta_data(year,month)
            final_data+=temp
            
            
                
        if year == 2013:        
            for i in range(len(final_data)-1):
                final_data[i].insert(8,aqi_final_13[i])
        elif year==2014:
            for i in range(len(final_data)-1):
                final_data[i].insert(8,aqi_final_14[i])
        elif year==2015:
            for i in range(len(final_data)-1):
                final_data[i].insert(8,aqi_final_15[i])
        elif year==2016:
            for i in range(len(final_data)-1):
                final_data[i].insert(8,aqi_final_16[i])
        elif year==2017:
            for i in range(len(final_data)-1):
                final_data[i].insert(8,aqi_final_17[i])
        elif year==2018:
            for i in range(len(final_data)-1):
                final_data[i].insert(8,aqi_final_18[i])
                
                
        
        with open('E:\Python_Learning\ML\Data_air_quality\Real_Data\combined_' +str(year)+ '.csv','w') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            wr.writerow(
                    ['T','TM','Tm','SLP','H','VV','V','VM','PM 2.5'])
        
            
            for row in final_data:
                flag=0
                for element in row:
                    if element == '' or element == '-':
                        flag=1
                if flag!=1:
                    wr.writerow(row)
    
    '''data_2013=combine_data(2013,600)
    data_2014=combine_data(2014,600)
    data_2015=combine_data(2015,600)
    data_2016=combine_data(2016,600)
    data_2017=combine_data(2017,600)
    data_2018=combine_data(2018,600)'''
    
    for years in range(2013,2019):
        total+=combine_data(years,600)
        
    #total=data_2013+data_2014+data_2015+data_2016+data_2017+data_2018
    
    with open('E:/Python_Learning/ML/Data_air_quality/Real_Data/Final_AQI_data.csv','w') as csvfile:
        wr=csv.writer(csvfile,dialect='excel')
        wr.writerow(['T','TM','Tm','SLP','H','VV','V','VM','PM 2.5'])
        wr.writerows(total)
        
        
        
    
    
                

            
                    
                
        
    
    
    
    
    