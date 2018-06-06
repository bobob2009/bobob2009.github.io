# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:05:21 2015

@author: michael
"""

import pandas as pd
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
import math
from collections import Counter
import pickle

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

wiki_urls = ['https://en.wikipedia.org/wiki/Orange_Revolution',
             'https://en.wikipedia.org/wiki/2014_Ukrainian_revolution',
             'https://en.wikipedia.org/wiki/2014_pro-Russian_unrest_in_Ukraine',
             'https://en.wikipedia.org/wiki/Boston_Tea_Party',
             'https://en.wikipedia.org/wiki/2004_Madrid_train_bombings',
             'https://en.wikipedia.org/wiki/American_Civil_War',
             'https://en.wikipedia.org/wiki/Western_Theater_of_the_American_Civil_War',
             'https://en.wikipedia.org/wiki/Eastern_Theater_of_the_American_Civil_War',
             'https://en.wikipedia.org/wiki/Peloponnesian_War',
             'https://en.wikipedia.org/wiki/Bay_of_Pigs_Invasion',
             'https://en.wikipedia.org/wiki/African-American_Civil_Rights_Movement_(1954%E2%80%9368)',
             'https://en.wikipedia.org/wiki/Brown_v._Board_of_Education',
             'https://en.wikipedia.org/wiki/Tokyo_subway_sarin_attack',
             'https://en.wikipedia.org/wiki/September_11_attacks',
             'https://en.wikipedia.org/wiki/Rwandan_Genocide',
             'https://en.wikipedia.org/wiki/Mau_Mau_Uprising',
             'https://en.wikipedia.org/wiki/Indonesia%E2%80%93Malaysia_confrontation',
             'https://en.wikipedia.org/wiki/Prohibition_in_the_United_States',
             'https://en.wikipedia.org/wiki/Second_Sino-Japanese_War',
             'https://en.wikipedia.org/wiki/Obergefell_v._Hodges',
             'https://en.wikipedia.org/wiki/Apollo_13',
             'https://en.wikipedia.org/wiki/Apollo_11']
             
#news_urls = ['http://www.bbc.com/news/world-europe-25210230',
#             'http://www.cnn.com/2013/11/04/world/europe/spain-train-bombings-fast-facts/',
#             'http://www.japantimes.co.jp/news/2015/03/20/national/tokyo-marks-20th-anniversary-of-aums-deadly-sarin-attack-on-subway-system/#.VlDvwN-rTVo']

news_urls = raw_input('Enter Article Url: ')

#news_urls = ['http://www.cnn.com/2013/11/04/world/europe/spain-train-bombings-fast-facts/']


#wiki_db = []
#for i in range(len(wiki_urls)):
#    data = alchemyapi.combined('url',wiki_urls[i],options={'extract':'page-image, entity, keyword, title, author, taxonomy, concept'})
#    wiki_db.append(data)

#article_url ='http://www.bbc.com/news/world-europe-25210230'
#wiki_data = alchemyapi.combined('url',article_url,options={'extract':'page-image, entity, keyword, title, author, taxonomy, concept' })


# take the wiki db and create the lists of terms(from entities and keywords and concepts) for each url/event

#d = []
#wiki_terms = pd.DataFrame(data=None,columns=['Title','URL','Entities','Keywords','Taxonomy','Concepts','Language','Author'])
#for i in range(len(wiki_db)):
#    d = [wiki_db[i]['title'],wiki_db[i]['url'],wiki_db[i]['entities'],wiki_db[i]['keywords'],wiki_db[i]['taxonomy'],wiki_db[i]['concepts'],wiki_db[i]['language'],wiki_db[i]['author']]
#    wiki_terms.loc[i]=d

#path = '/Users/michael/PycharmProjects/Startup Weekend/'
#wiki_terms.to_pickle('wiki_terms.pk1')
#wiki_terms.to_csv('wiki_terms2.csv')
wiki_terms = pd.read_pickle('wiki_terms.pk1')
#wiki_terms2 = pd.read_csv('wiki_terms2.csv')


news = alchemyapi.combined('url',news_urls,options={'extract':'page-image, entity, keyword, title, author, taxonomy, concept'})
news_keywords = []
for i in range(len(news['keywords'])):
    news_keywords.append(news['keywords'][i]['text'])
    
for i in range(len(news['entities'])):
    news_keywords.append(news['entities'][i]['text'])
    
for i in range(len(news['concepts'])):
    news_keywords.append(news['concepts'][i]['text'])

news_list = Counter(news_keywords)
wiki_list1 = []
wiki_list2 = []
wiki_list3 = []
wiki_list4 = []
wiki_list5 = []
wiki_list6 = []
wiki_list7 = []
wiki_list8 = []
wiki_list9 = []
wiki_list10 = []
wiki_list11 = []
wiki_list12 = []
wiki_list13 = []
wiki_list14 = []
wiki_list15 = []
wiki_list16 = []
wiki_list17 = []
wiki_list18 = []
wiki_list19 = []
wiki_list20 = []
wiki_list21 = []
wiki_list22 = []

#for j in range(len(wiki_terms['Keywords'])):
#    for i in range(len(wiki_terms['Keywords'][j])):
#        wiki_list1.append(wiki_terms['Keywords'][0][i]['text'])
#        wiki_list1.append(wiki_terms['Entities'][0][i]['text'])

for i in range(len(wiki_terms['Keywords'][0])):
    wiki_list1.append(wiki_terms['Keywords'][0][i]['text'])
    wiki_list1.append(wiki_terms['Entities'][0][i]['text'])
for j in range(len(wiki_terms['Concepts'][0])):
    wiki_list1.append(wiki_terms['Concepts'][0][j]['text'])
        
for i in range(len(wiki_terms['Keywords'][1])):
    wiki_list2.append(wiki_terms['Keywords'][1][i]['text'])
    wiki_list2.append(wiki_terms['Entities'][1][i]['text'])
for j in range(len(wiki_terms['Concepts'][1])):
    wiki_list2.append(wiki_terms['Concepts'][1][j]['text'])
        
for i in range(len(wiki_terms['Keywords'][2])):
    wiki_list3.append(wiki_terms['Keywords'][2][i]['text'])
    wiki_list3.append(wiki_terms['Entities'][2][i]['text'])
for j in range(len(wiki_terms['Concepts'][2])):
    wiki_list3.append(wiki_terms['Concepts'][2][j]['text'])
        
for i in range(len(wiki_terms['Keywords'][3])):
    wiki_list4.append(wiki_terms['Keywords'][3][i]['text'])
    wiki_list4.append(wiki_terms['Entities'][3][i]['text'])
for j in range(len(wiki_terms['Concepts'][3])):
    wiki_list4.append(wiki_terms['Concepts'][3][j]['text'])
        
for i in range(len(wiki_terms['Keywords'][4])):
    wiki_list5.append(wiki_terms['Keywords'][4][i]['text'])
    wiki_list5.append(wiki_terms['Entities'][4][i]['text'])
for j in range(len(wiki_terms['Concepts'][4])):
    wiki_list5.append(wiki_terms['Concepts'][4][j]['text'])
        
for i in range(len(wiki_terms['Keywords'][5])):
    wiki_list6.append(wiki_terms['Keywords'][5][i]['text'])
    wiki_list6.append(wiki_terms['Entities'][5][i]['text'])
for j in range(len(wiki_terms['Concepts'][5])):
    wiki_list6.append(wiki_terms['Concepts'][5][j]['text'])
        
for i in range(len(wiki_terms['Keywords'][6])):
    wiki_list7.append(wiki_terms['Keywords'][6][i]['text'])
    wiki_list7.append(wiki_terms['Entities'][6][i]['text'])
for j in range(len(wiki_terms['Concepts'][6])):
    wiki_list7.append(wiki_terms['Concepts'][6][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][7])):
    wiki_list8.append(wiki_terms['Keywords'][7][i]['text'])
    wiki_list8.append(wiki_terms['Entities'][7][i]['text'])
for j in range(len(wiki_terms['Concepts'][7])):
    wiki_list8.append(wiki_terms['Concepts'][7][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][8])):
    wiki_list9.append(wiki_terms['Keywords'][8][i]['text'])
    wiki_list9.append(wiki_terms['Entities'][8][i]['text'])
for j in range(len(wiki_terms['Concepts'][8])):
    wiki_list9.append(wiki_terms['Concepts'][8][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][9])):
    wiki_list10.append(wiki_terms['Keywords'][9][i]['text'])
    wiki_list10.append(wiki_terms['Entities'][9][i]['text'])
for j in range(len(wiki_terms['Concepts'][9])):
    wiki_list10.append(wiki_terms['Concepts'][9][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][10])):
    wiki_list11.append(wiki_terms['Keywords'][10][i]['text'])
    wiki_list11.append(wiki_terms['Entities'][10][i]['text'])
for j in range(len(wiki_terms['Concepts'][10])):
    wiki_list11.append(wiki_terms['Concepts'][10][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][11])):
    wiki_list12.append(wiki_terms['Keywords'][11][i]['text'])
    wiki_list12.append(wiki_terms['Entities'][11][i]['text'])
for j in range(len(wiki_terms['Concepts'][11])):
    wiki_list12.append(wiki_terms['Concepts'][11][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][12])):
    wiki_list13.append(wiki_terms['Keywords'][12][i]['text'])
    wiki_list13.append(wiki_terms['Entities'][12][i]['text'])
for j in range(len(wiki_terms['Concepts'][12])):
    wiki_list13.append(wiki_terms['Concepts'][12][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][13])):
    wiki_list14.append(wiki_terms['Keywords'][13][i]['text'])
    wiki_list14.append(wiki_terms['Entities'][13][i]['text'])
for j in range(len(wiki_terms['Concepts'][13])):
    wiki_list14.append(wiki_terms['Concepts'][13][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][14])):
    wiki_list15.append(wiki_terms['Keywords'][14][i]['text'])
    wiki_list15.append(wiki_terms['Entities'][14][i]['text'])
for j in range(len(wiki_terms['Concepts'][14])):
    wiki_list15.append(wiki_terms['Concepts'][14][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][15])):
    wiki_list16.append(wiki_terms['Keywords'][15][i]['text'])
    wiki_list16.append(wiki_terms['Entities'][15][i]['text'])
for j in range(len(wiki_terms['Concepts'][15])):
    wiki_list16.append(wiki_terms['Concepts'][15][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][16])):
    wiki_list17.append(wiki_terms['Keywords'][16][i]['text'])
    wiki_list17.append(wiki_terms['Entities'][16][i]['text'])
for j in range(len(wiki_terms['Concepts'][16])):
    wiki_list17.append(wiki_terms['Concepts'][16][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][17])):
    wiki_list18.append(wiki_terms['Keywords'][17][i]['text'])
    wiki_list18.append(wiki_terms['Entities'][17][i]['text'])
for j in range(len(wiki_terms['Concepts'][17])):
    wiki_list18.append(wiki_terms['Concepts'][17][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][18])):
    wiki_list19.append(wiki_terms['Keywords'][18][i]['text'])
    wiki_list19.append(wiki_terms['Entities'][18][i]['text'])
for j in range(len(wiki_terms['Concepts'][18])):
    wiki_list19.append(wiki_terms['Concepts'][18][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][19])):
    wiki_list20.append(wiki_terms['Keywords'][19][i]['text'])
    wiki_list20.append(wiki_terms['Entities'][19][i]['text'])
for j in range(len(wiki_terms['Concepts'][19])):
    wiki_list20.append(wiki_terms['Concepts'][19][j]['text'])
    
for i in range(len(wiki_terms['Keywords'][20])):
    wiki_list21.append(wiki_terms['Keywords'][20][i]['text'])
    wiki_list21.append(wiki_terms['Entities'][20][i]['text'])
for j in range(len(wiki_terms['Concepts'][20])):
    wiki_list21.append(wiki_terms['Concepts'][20][j]['text'])
        
for i in range(len(wiki_terms['Keywords'][21])):
    wiki_list22.append(wiki_terms['Keywords'][21][i]['text'])
    wiki_list22.append(wiki_terms['Entities'][21][i]['text'])
for j in range(len(wiki_terms['Concepts'][21])):
    wiki_list22.append(wiki_terms['Concepts'][21][j]['text'])


# define list 2 and then do counter_cosine...

cwiki_list1 = Counter(wiki_list1)
cwiki_list2 = Counter(wiki_list2)
cwiki_list3 = Counter(wiki_list3)
cwiki_list4 = Counter(wiki_list4)
cwiki_list5 = Counter(wiki_list5)
cwiki_list6 = Counter(wiki_list6)
cwiki_list7 = Counter(wiki_list7)
cwiki_list8 = Counter(wiki_list8)
cwiki_list9 = Counter(wiki_list9)
cwiki_list10 = Counter(wiki_list10)
cwiki_list11 = Counter(wiki_list11)
cwiki_list12 = Counter(wiki_list12)
cwiki_list13 = Counter(wiki_list13)
cwiki_list14 = Counter(wiki_list14)
cwiki_list15 = Counter(wiki_list15)
cwiki_list16 = Counter(wiki_list16)
cwiki_list17 = Counter(wiki_list17)
cwiki_list18 = Counter(wiki_list18)
cwiki_list19 = Counter(wiki_list19)
cwiki_list20 = Counter(wiki_list20)
cwiki_list21 = Counter(wiki_list21)
cwiki_list22 = Counter(wiki_list22)

score1 = counter_cosine_similarity(news_list,cwiki_list1)
score2 = counter_cosine_similarity(news_list,cwiki_list2)
score3 = counter_cosine_similarity(news_list,cwiki_list3)
score4 = counter_cosine_similarity(news_list,cwiki_list4)
score5 = counter_cosine_similarity(news_list,cwiki_list5)
score6 = counter_cosine_similarity(news_list,cwiki_list6)
score7 = counter_cosine_similarity(news_list,cwiki_list7)
score8 = counter_cosine_similarity(news_list,cwiki_list8)
score9 = counter_cosine_similarity(news_list,cwiki_list9)
score10 = counter_cosine_similarity(news_list,cwiki_list10)
score11 = counter_cosine_similarity(news_list,cwiki_list11)
score12 = counter_cosine_similarity(news_list,cwiki_list12)
score13 = counter_cosine_similarity(news_list,cwiki_list13)
score14 = counter_cosine_similarity(news_list,cwiki_list14)
score15 = counter_cosine_similarity(news_list,cwiki_list15)
score16 = counter_cosine_similarity(news_list,cwiki_list16)
score17 = counter_cosine_similarity(news_list,cwiki_list17)
score18 = counter_cosine_similarity(news_list,cwiki_list18)
score19 = counter_cosine_similarity(news_list,cwiki_list19)
score20 = counter_cosine_similarity(news_list,cwiki_list20)
score21 = counter_cosine_similarity(news_list,cwiki_list21)
score22 = counter_cosine_similarity(news_list,cwiki_list22)

scores = pd.DataFrame(None,columns=['Title','Score'],index=[0]*22)
for i in range(len(wiki_terms['Title'])):
    scores.iloc[i,0] = wiki_terms['Title'][i]
    
scores.iloc[0,1] = score1
scores.iloc[1,1] = score2
scores.iloc[2,1] = score3
scores.iloc[3,1] = score4
scores.iloc[4,1] = score5
scores.iloc[5,1] = score6
scores.iloc[6,1] = score7
scores.iloc[7,1] = score8
scores.iloc[8,1] = score9
scores.iloc[9,1] = score10
scores.iloc[10,1] = score11
scores.iloc[11,1] = score12
scores.iloc[12,1] = score13
scores.iloc[13,1] = score14
scores.iloc[14,1] = score15
scores.iloc[15,1] = score16
scores.iloc[16,1] = score17
scores.iloc[17,1] = score18
scores.iloc[18,1] = score19
scores.iloc[19,1] = score20
scores.iloc[20,1] = score21
scores.iloc[21,1] = score22

scores_sorted = scores.sort(['Score'],ascending=0)

print scores_sorted
    
#int_14 = set(news_list).intersection(list4)
    

#list1=[]
#for i in range(len(test['entities'])):
#    list1.append(test['entities'][i]['text'])
#    
#for i in range(len(test['concepts'])):
#    print test['concepts'][i]['text']
#    
#for i in range(len(test['keywords'])):
#    print test['keywords'][i]['text']
#    
# KEYWORDS MIGHT BE BETTER, OR AT LEAST COMBINE ENTITIES AND KEYWORDS