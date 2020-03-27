# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:13:42 2020

@author: Omkaar
"""

import os
import requests
import time
import sys

#automating the data collection by iterating through years and months
def retrieve_html():
    for year in range(2000,2019):
        for month in range(1,13):
            if (month <10):
                url='https://en.tutiempo.net/climate/0{}-{}/ws-430630.html'.format(month,year)
            else:
                url='https://en.tutiempo.net/climate/{}-{}/ws-430630.html'.format(month,year)
                
                
            source_text=requests.get(url) #storing all the html pages in source_text
            text_utf=source_text.text.encode('utf=8') #to take of the some utf encoding in the html pages
        
            if not os.path.exists('E:/Python_Learning/ML/Data_air_quality/{}'.format(year)):
                os.makedirs('E:/Python_Learning/ML/Data_air_quality/{}'.format(year))
            with open('E:/Python_Learning/ML/Data_air_quality/{}/{}.html'.format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
        
        
 if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print('Time taken {}'.format(stop_time-start_time))
        
                