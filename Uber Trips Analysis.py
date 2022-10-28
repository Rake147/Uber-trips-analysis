#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv('C:/Users/Rakesh/Datasets/uber-raw-data-sep14.csv')


# In[3]:


data.head()


# In[5]:


data["Date/Time"] = data["Date/Time"].map(pd.to_datetime) 
data.head()


# In[7]:


data['Day']=data['Date/Time'].apply(lambda x: x.day)
data['Weekday']=data['Date/Time'].apply(lambda x: x.weekday())
data['Hour']=data['Date/Time'].apply(lambda x: x.hour)
data.head(20)


# In[11]:


sns.set(rc={'figure.figsize':(12,10)})
sns.distplot(data['Day'])


# In[12]:


sns.distplot(data['Hour'])


# In[13]:


sns.distplot(data['Weekday'])


# In[15]:


df=data.groupby(['Weekday','Hour']).apply(lambda x: len(x))
df=df.unstack()
sns.heatmap(df,annot=False)


# In[20]:


data.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data['Day'], label='Uber Trips',
figsize=(12, 8), cmap=plt.get_cmap('jet'))
plt.title("Uber Trips Analysis")
plt.legend()
plt.show()


# ## Summary
# 1.Monday is the most profitable day for Uber
# 
# 2.On Saturdays less number of people use Uber
# 
# 3.6 pm is the busiest day for Uber
# 
# 4.On average a rise in Uber trips start around 5 am.
# 
# 5.Most of the Uber trips originate near the Manhattan region in New York.

# In[ ]:




