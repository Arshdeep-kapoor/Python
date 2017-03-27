
# coding: utf-8

# In[32]:

############
import pandas as pd
import numpy as np


# In[33]:

trainData = pd.read_csv('pvaBal35Trg.csv')


# In[34]:

print(trainData.head())


# In[35]:

trainData['ZIP'] = trainData['ZIP'].abs()


# In[ ]:




# In[36]:

count = 0
for z in trainData.ZIP:
    if z < 0:
        count = count + 1
print (count)


# In[37]:

print(trainData['ZIP'].dtype)


# In[38]:

print((trainData['ZIP'][0] /  10000))


# In[39]:

trainData['ZIP1'] = (trainData['ZIP'] /  10000)


# In[40]:

trainData['ZIP23'] = (trainData['ZIP'] %  10000) / 100


# In[41]:

print(trainData.head())


# In[ ]:




# In[42]:

trainData['ZIP1'] = trainData['ZIP1'].apply(np.floor)


# In[43]:

trainData['ZIP23'] = trainData['ZIP23'].apply(np.floor)


# In[44]:

trainData['ZIP1'] = trainData['ZIP1'].apply(int)
trainData['ZIP23'] = trainData['ZIP23'].apply(int)


# In[45]:

print(trainData['DOMAIN'].fillna('U4',inplace=True)


# In[46]:

print(trainData.DOMAIN)


# In[47]:

print (trainData.count())  #### returns non null values of each column
print (trainData.shape)


# In[48]:

trainData.fillna(0,inplace=True)


# In[49]:

print (trainData.count()) 


# In[50]:

del trainData['ZIP']


# In[51]:

print(trainData.head())


# In[52]:

print (type(trainData))


# In[53]:

print(trainData.GENDER.unique())


# In[54]:

trainData.ix[trainData.GENDER == 0, 'GENDER'] = 'U'


# In[55]:

trainData.GENDER.unique()


# In[56]:

trainData.head()


# In[57]:

trainData.MAJOR.unique()


# In[58]:

trainData.ix[trainData.MAJOR == 'X', 'MAJOR'] = 1


# In[59]:

trainData.MAJOR.unique()


# In[60]:

trainData.MDMAUD.unique()


# In[61]:

trainData.ix[trainData.MDMAUD == 'XXXX', 'MDMAUD'] = 0
trainData.ix[trainData.MDMAUD == 'C1CM', 'MDMAUD'] = 1


# In[62]:

trainData.MDMAUD.unique()


# In[63]:

trainData = trainData.drop(['ODATEDW','OSOURCE','TCODE','NOEXCH','AGEFLAG','DATASRCE','SOLP3','SOLIH','GEOCODE','COLLECT1'],axis = 1)


# In[64]:

trainData = trainData.drop(['BIBLE', 'CATLG', 'HOMEE', 'PETS', 'CDPLAY', 'STEREO', 
                            'PCOWNERS', 'PHOTO', 'CRAFTS', 'FISHER', 'GARDENIN', 'BOATS', 'WALKER', 
                            'KIDSTUFF', 'CARDS', 'PLATES', 'LIFESRC'],axis = 1)


# In[65]:

trainData = trainData.drop(['CARDPROM', 'MINRAMNT', 'MINRDATE' , 'MAXRDATE', 'LASTGIFT', 'LASTDATE', 'FISTDATE', 
                            'NEXTDATE', 'TIMELAG', 'CONTROLN', 'HPHONE_D', 'MDMAUD_R', 'MDMAUD_F', 'MDMAUD_A', 
                            'CLUSTER2', 'GEOCODE2' , 'PVASTATE' , 'RECINHSE' , 'RECP3' , 'RECPGVG', 
                            'RECSWEEP' , 'CLUSTER' , 'HIT' , 'PEPSTRFL' , 'AFC1', 'AFC1' , 'NUMPRM12' 
                            , 'NGIFTALL' , 'CARDGIFT'],axis = 1)


# In[66]:

trainData = trainData.drop(['AGE901','AGE902','AGE903','AGE904','AGE905','AGE906','AGE907', 'CHIL1','CHIL2' ,'CHIL3',
                            'AGEC1','AGEC2','AGEC3', 'AGEC4', 'AGEC5', 'AGEC6', 'AGEC7', 'CHILC1','CHILC2',
                            'CHILC3','CHILC4','CHILC5', 'HHAGE1','HHAGE2','HHAGE3', 'HHN1','HHN2','HHN3','HHN4','HHN5',
                            'HHN6', 'MARR1','MARR2','MARR3','MARR4', 'HHP1', 'HHP2', 'DW1','DW2','DW3','DW4','DW5',
                            'DW6','DW7','DW8','DW9','HU1','HU2','HU3','HU4','HU5', 'HHD1','HHD2','HHD3','HHD4','HHD5',
                            'HHD6','HHD7','HHD8','HHD9','HHD10','HHD11','HHD12', 'ETHC1','ETHC2','ETHC3','ETHC4','ETHC5',
                            'ETHC6','HVP1','HVP2','HVP3','HVP4','HVP5','HVP6','HUR1', 'HUR2', 
                            'RHP1','RHP2','RHP3'],axis = 1)


# In[67]:

trainData.head()


# In[68]:

trainData.shape


# In[69]:

trainData.corr()['TARGET_B']


# In[ ]:




# In[70]:

good_columns = trainData[['ETH1','ETH2','ETH3','ETH4','ETH5','ETH6','ETH7','ETH8',
                         'ETH9','ETH10','ETH11','ETH12','ETH13','ETH14','ETH15','ETH16','EIC1','EIC2','EIC3',
                         'EIC4','EIC5','EIC6','EIC7','EIC8','EIC9','EIC10','EIC11',
                         'EIC12','EIC13','EIC14','EIC15','EIC16']]

trainData = trainData.drop(['ETH1','ETH2','ETH3','ETH4','ETH5','ETH6','ETH7','ETH8',
                         'ETH9','ETH10','ETH11','ETH12','ETH13','ETH14','ETH15','ETH16','EIC1','EIC2','EIC3',
                         'EIC4','EIC5','EIC6','EIC7','EIC8','EIC9','EIC10','EIC11',
                         'EIC12','EIC13','EIC14','EIC15','EIC16'],axis = 1)

print (good_columns)


# In[71]:

trainData.shape


# In[72]:

# Import the PCA model.
from sklearn.decomposition import PCA

# Create a PCA model.
pca_4 = PCA(n_components=4)
# Fit the PCA model on the numeric columns from earlier.
after_pca = pca_4.fit(good_columns)


# In[73]:

print (after_pca.explained_variance_ratio_)
print (after_pca.components_)
print (after_pca.n_components)


# In[74]:

after_pca_transform = after_pca.transform(good_columns)


# In[75]:

after_pca_transform


# In[76]:

after_pca_transform.shape


# In[77]:

pca_columns = ['pca1','pca2','pca3','pca4']
df2 = pd.DataFrame(data=after_pca_transform, columns=pca_columns)


# In[78]:

newTrain = trainData.merge(df2,how='inner', left_index=True, right_index=True)


# In[79]:

print (newTrain.head())


# In[80]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[81]:

plt.plot(trainData.AGE)


# In[82]:

plt.scatter(trainData.AGE,trainData.TARGET_B)


# In[83]:

trainData['GENDER'] = trainData['GENDER'].astype(str)


# In[88]:

xvalues = trainData['GENDER'].unique()


# In[89]:

import seaborn as sns


# In[90]:

sns.countplot(x=trainData['GENDER'],data=trainData)


# In[93]:

newTrain.head()


# In[94]:

target = newTrain['TARGET_B']


# In[95]:

data = newTrain.drop('TARGET_B',axis = 1)


# In[96]:

data.head()


# In[97]:

target.head()


# In[98]:

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data,target,test_size = 0.4, random_state = 4)


# In[99]:

print (data.shape)
print(target.shape)
print (X_train.shape)
print (y_train.shape)


# In[100]:

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()


# In[102]:

X_train.dtypes


# In[ ]:



