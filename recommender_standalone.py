import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
stringg='Fargo'
print("Calculating recommendations for...    " + stringg+":")

pd.set_option('display.max_columns', 100)
newdataframe = pd.read_csv('c.csv', encoding ="UTF8")
newdataframe.head()



newdataframe.shape



newdataframe = newdataframe[['Title','Genre','Director','Actors','Plot']]
newdataframe.head()




newdataframe.shape




newdataframe['Actors'] = newdataframe['Actors'].map(lambda x: x.split(',')[:3])
newdataframe['Genre'] = newdataframe['Genre'].map(lambda x: x.lower().split(','))
newdataframe['Director'] = newdataframe['Director'].map(lambda x: x.split(' '))


for index, row in newdataframe.iterrows():
    row['Actors'] = [x.lower().replace(' ','') for x in row['Actors']]
    row['Director'] = ''.join(row['Director']).lower()







newdataframe['Key_words'] = ""

for index, row in newdataframe.iterrows():
    plot = row['Plot']
    
    rake_instance = Rake()

    rake_instance.extract_keywords_from_text(plot)

    key_words_dict_scores = rake_instance.get_word_degrees()

    row['Key_words'] = list(key_words_dict_scores.keys())


newdataframe.drop(columns = ['Plot'], inplace = True)




newdataframe.set_index('Title', inplace = True)
newdataframe.head()




newdataframe['bow'] = ''
columns = newdataframe.columns
for index, row in newdataframe.iterrows():
    words = ''
    for col in columns:
        if col != 'Director':
            words = words + ' '.join(row[col])+ ' '
        else:
            words = words + row[col]+ ' '
    row['bow'] = words
    
newdataframe.drop(columns = [col for col in newdataframe.columns if col!= 'bow'], inplace = True)




newdataframe.head()




count = CountVectorizer()
cmatrix = count.fit_transform(newdataframe['bow'])

point = pd.Series(newdataframe.index)
point[:5]





cs = cosine_similarity(cmatrix, cmatrix)
cs




def recommendations(title, cosine_sim = cs):
    
    r = []
    
    
    idx = point[point == title].index[0]

    #similarity scores in descending order
    ss = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    
    top10 = list(ss.iloc[1:11].index)
    
    for i in top10:
        r.append(list(newdataframe.index)[i])
        
    return r




x=recommendations(stringg)
print (*x, sep= "\n")
