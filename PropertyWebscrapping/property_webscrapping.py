# import beautifulsoup4 & connection requests library
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import re
from time import sleep
import random
sns.set()
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
			
			
			
			
name = []
#created = []
prices = []
areas = []
configuration = []
other_info = []
descriptions = []
urls = []
thumbnails =[]

# define city
city = 'Pune'
locality='Hinjewadi'



##%%time
page=0
for pagenum in range(1,52):
    page+=1
    firstPage_url ='https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&Locality='+locality+'&cityName='+city+'&page='+str(pagenum)
    response=get(firstPage_url,headers=headers)
    html_soup=BeautifulSoup(response.text,'html.parser')


    house_containers = html_soup.find_all('div', class_="l-srp__results flex__item")
    #house_containers = html_soup.find_all('div', class_="m-srp-card SRCard")
    #house_containers = html_soup.find_all('div', class_="flex relative clearfix m-srp-card__container")
    #house_containers = html_soup.find_all('div', class_="l-srp__wrap l-srp__wrap__tvsCampaign") 
    #t=house_containers[0]
    #t.find_all('div',class_='m-srp-card__description js-content-read-more truncated')
    if house_containers !=[]:
        for t in house_containers:
            for url in t.find_all('img'):
                thumbnails.append(str(url))

            for url in t.find_all('a'):
                urls.append(url.get('href'))
                name.append(url)

            for price in t.find_all('div',class_='m-srp-card__price'):
                prices.append(price)

            for other_infos in t.find_all('div',class_='m-srp-card__summary__item'):
                other_info.append(other_infos)

            for config in t.find_all(class_='m-srp-card__title__bhk'):
                configuration.append(config)

            for description in t.find_all('div',class_='m-srp-card__description js-content-read-more truncated'):
                descriptions.append(description)
                
    else:
        break
    sleep(random.randint(1,200))
    
    
print('You scraped {} pages containing {} properties.'.format(page, len(name)))
print(len(name))
print(len(created))
print(len(prices ))
print(len(areas ))
print(len(configuration)) 
print(len(other_info))
print(len(descriptions)) 
print(len(urls)) 
print(len(thumbnails ))



###Cleaning the data

clean_name=[]
for i in name:
    for j in i:
        clean_name.append(j)


clean_price=[]
for i in prices:
    for j in i:
        clean_price.append(j)
        

clean_configuration=[]
for i in configuration:
    for j in i:
        clean_configuration.append(''.join(j.split()))

    

clean_other_info=[]
for i in other_info:
    for j in i:
        new_other_info.append(''.join(str(j).split()).strip())

new_other_info=[x for x in new_other_info if x]

tag_re = re.compile(r'<[^>]+>')
def remove_tags(text):
    return tag_re.sub('', text)

clean_other_info=[]
for i in new_other_info:
    clean_other_info.append(remove_tags(i))

#clean_other_info=list(filter(None,clean_other_info))

#for ind,i in enumerate(clean_other_info):
    #if i[0]=='<':
        #clean_other_info.remove(clean_other_info[ind])

areas=[some_other_info[ind+1] for ind,i in enumerate(some_other_info) if i=='carpetarea' ]

num_floor=[some_other_info[ind+1] for ind,i in enumerate(some_other_info) if i=='floor' ]

transaction_type=[some_other_info[ind+1] for ind,i in enumerate(some_other_info) if i=='transaction' ]

furnishing_type=[some_other_info[ind+1] for ind,i in enumerate(some_other_info) if i=='furnishing' ]

society_name=[some_other_info[ind+1] for ind,i in enumerate(some_other_info) if i=='society' ]

bathroom_num=[some_other_info[ind+1] for ind,i in enumerate(some_other_info) if i=='bathroom' ]

status=[some_other_info[ind+1] for ind,i in enumerate(some_other_info) if i=='status' ]

clean_description=[]
for i in descriptions:
    for j in i:
        clean_description.append(str(j).strip())
        
#clean_description=list(filter(None,clean_description[0::2]))[0::2]
clean_description=[x for x in clean_description if x][0::2]

#Creating dataframe

Flat_dict={
'Name':clean_name,
'Price':clean_price ,
'Area':areas ,
'Configuration':clean_configuration ,
'Description':clean_description ,
'Url':urls ,
'Image':thumbnails ,
'Num_of_floors':num_floor,
'Transaction_type':transaction_type,
'Furnishing_type':furnishing_type,
'Society_name':society_name,
'Bathroom_num':bathroom_num,
'Status':status
}

Flat_list=pd.DataFrame.from_dict(Flat_dict,orient='index').T.dropna()
Flat_list.to_excel('flat_list_raw.xls')