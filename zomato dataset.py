#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis

# # zomato dataset

# In[19]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[20]:


df = pd.read_csv('zomato.csv',encoding='latin-1')


# In[21]:


df


# In[22]:


df.head()


# In[23]:


df.columns


# In[24]:


df.info()


# In[25]:


df.describe()

## basic information in data analysis what all things we do
# missing values
2 Explore about the numerical variables
3 explore about catagorical variables
4 finding relationship between features
# In[26]:


df.shape


# In[27]:


df.isnull().sum()

# If you want to do anything with respect to the missing value you will 
basically have to work on that missing value# another way  i will just write a simple code which will actually\
tell me all the information,all the features that has missing values.so what i can basically do
# In[28]:


[features for features in df.columns if df[features].isnull().sum()>0]  # list comprehension


# In[29]:


# with the help of heat  map we can also find missing values
sns.heatmap(df.isnull(),yticklabels = False,cbar= False,cmap='viridis')


# In[30]:


df_country = pd.read_excel("Country_Code.xlsx")
df_country.head()


# In[31]:


df.columns


# In[32]:


final_df = pd.merge(df,df_country,on='Country Code',how='left')


# In[33]:


final_df.head(2)


# In[34]:


## there is only another way to check data types
final_df.dtypes


# In[35]:


final_df.columns


# In[36]:


final_df[['Country Code']]


# In[37]:


final_df.Country.value_counts()


# In[38]:


country_names = final_df.Country.value_counts().index


# In[39]:


country_val = final_df.Country.value_counts().values


# In[40]:


# Pie chart - Top three countries that uses zomato

plt.pie(country_val[:3],labels = country_names[:3],autopct="%1.2f%%")

observation: Zomato maximum records or transactions are from india with a percentage of (94.39%)
after that usa with a percentage of (4.73%) and then united kingdom which has a percentage of (0.87%).
# In[41]:


final_df.columns


# In[42]:


ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns = {0:'Rating Count'})


# In[43]:


ratings

Conclusions/observations
whenever the rating is from 4.5 4.9 it indicates that it is excellent
2.when the rating is from between 4.0 to 4.4 it is very goood
3. When rating is between 3.5 to 3.9 it means it is good
4. When rating is between 3.0 to 3.4 it means it is average
5. When rating is between 2.5 to 2.9 it means it is average
6. When rating is between 3.0 to 2.4 it means it is poor

# In[44]:


ratings.head()


# In[45]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x = "Aggregate rating",y = "Rating Count",data = ratings)


# In[46]:


sns.barplot(x = "Aggregate rating",y = "Rating Count",hue = 'Rating color',data = ratings,palette=['white','red','orange','yellow','green','green'])

observation:
1. Not Rated count is very high 
2. Maximum number of ratings are between 2.5 to 3.4

# In[47]:


# cpount plot
sns . countplot(x= "Rating color",data = ratings ,palette=['blue','red','orange','yellow','green','green'])


# In[48]:


ratings


# In[56]:


# find the countries that has given zero rating
final_df.head(2)
final_df.columns


# In[61]:


final_df[final_df["Rating color"] == 'White'].groupby("Country").size().reset_index()


# In[63]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)

observation:
1.maximum number of zero ratings are from indian customers
# In[66]:


# find out which currency is used by which country
final_df.columns


# In[68]:


final_df.groupby(['Country','Currency']).size().reset_index()


# In[70]:


# which country do have online deliveries option?
final_df.groupby(['Country','Currency','Has Online delivery']).size().reset_index()

observation:
the main two country which has the online deliveries are india and uae
# In[81]:


final_df.columns


# In[83]:


# create a pie chart for cities distribution?
city_labels = final_df.City.value_counts().index


# In[87]:


city_values =final_df.City.value_counts().values


# In[92]:


plt.pie(city_values[:5], labels = city_labels[:5],autopct="%1.2f%%")


# In[93]:


# find the top ten cuisines?
final_df.columns


# In[104]:


final_df.groupby(['City','Country','Cuisines'[:10]]).size().reset_index().head(10)


# In[ ]:




