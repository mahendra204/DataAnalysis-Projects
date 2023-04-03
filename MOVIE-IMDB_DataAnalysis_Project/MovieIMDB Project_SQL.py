#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
database='movies.sqlite'


# In[5]:


connection=sqlite3.connect(database)
table=pd.read_sql(""" select * from 
                sqlite_master where type='table'""", connection)
table


# In[8]:


movies=pd.read_sql(''' select * from movies''', connection)
movies


# In[10]:


movies.size


# In[12]:


movies.shape


# In[13]:


movies.tail()


# In[14]:


movies.info()


# In[15]:


movies.describe()


# In[18]:


movies.dtypes


# In[22]:


movies.isnull().sum()


# In[32]:


movies.info()


# In[68]:


moviedetails=movies[['id','original_title','budget']]
moviedetails


# In[69]:


moviebudgetlist=moviedetails[moviedetails['budget']>10000000]
moviebudgetlist


# In[71]:


moviebudgetlist.head(15)


# In[74]:


moviebudgetlist.sort_values(by='budget',ascending=False).head(20)


# In[70]:


directors=pd.read_sql(''' select * from directors''', connection)
directors


# In[76]:


directors.info()


# In[77]:


directors.isnull().sum()


# In[79]:


movies.isnull().sum()


# In[80]:


directors


# In[81]:


movies


# In[85]:


directors_movies = pd.read_sql("""SELECT *
                        FROM directors
                        JOIN movies ON directors.id = movies.director_id;""", connection)
directors_movies.head(10)


# In[84]:


directors_movies.info()


# In[86]:


directors_movies.describe()


# In[89]:


movies_count=pd.read_sql(''' select count(*) as total_number_of_movies from movies''',connection)
movies_count


# In[94]:


directors_count=pd.read_sql(''' select count(*) as total_number_of_directors from directors group by gender''', connection)
directors_count


# In[98]:


specific_directors=pd.read_sql(''' SELECT d.name,m.title,m.budget from directors d join movies m on 
d.id=m.director_id ''', connection)
specific_directors


# In[101]:


specific_directors=pd.read_sql('''SELECT * from directors where name == 'James Cameron' or
name =='Luc Besson' or name =='John Woo' ''',connection)
specific_directors


# In[110]:


specific_directors=pd.read_sql('''SELECT m.title,d.name  from directors d join movies m
on d.id=m.director_id ''',connection)
specific_directors


# In[111]:


pd.read_sql(''' select * from directors where name LIKE 'Steven%' ''' , connection)


# In[113]:


pd.read_sql(''' select * from directors where name LIKE 'james%' ''' , connection)


# In[115]:


pd.read_sql('''select count(*) as female_directors from directors where gender == 1''',connection)


# In[116]:


pd.read_sql('''select count(*) as male_directors from directors where gender == 2''',connection)


# In[117]:


pd.read_sql('''select count(*) as transgender_directors from directors where gender == 0''',connection)


# In[119]:


pd.read_sql('''select count(*) as no_of_directors from directors''',connection)


# In[127]:


pd.read_sql('''select d.name,m.title from directors d join movies m on d.id=m.director_id
WHERE gender == 1
ORDER by  d.id asc 
limit 10 OFFSET 10''',connection)


# In[130]:


popular_movies=pd.read_sql(''' select original_title, popularity from movies order by popularity''', connection)


# In[135]:


popular_movies.sort_values(by='popularity', ascending=False).head(10)


# In[143]:


pd.read_sql('''SELECT m.popularity, m.original_title, d.name from directors d join movies m on m.director_id =d.id
ORDER by popularity desc   
limit 5''', connection)


# In[154]:


pd.read_sql(''' select d.name,m.original_title,m.budget from movies m join directors d on d.id=m.director_id 
order by budget desc''', connection).head(5)


# In[168]:


movie_vote=pd.read_sql(''' select original_title,vote_count,vote_average from movies
where release_date > '2000-01-01'
ORDER by vote_average desc
limit 10''',connection)
movie_vote.sort_values(by='vote_count',ascending=False)


# In[207]:


pd.read_sql('''select d.name,m.release_date, m.original_title,m.budget from movies m 
join directors d ON d.id = m.director_id
where d.name like 'james%ron' and release_date < '2015-12-10' order by release_date''',connection)


# In[200]:


pd.read_sql(''' select d.name,count(d.name) from directors d join movies m on m.director_id=d.id 
group by director_id ORDER BY count(d.name) DESC
limit 100''',connection)


# In[209]:


pd.read_sql(''' select d.name,m.budget from directors d join movies m on m.director_id=d.id
group by director_id order by sum(budget) desc limit 100''', connection).head(10)


# In[ ]:




