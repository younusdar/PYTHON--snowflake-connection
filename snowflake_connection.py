#!/usr/bin/env python
# coding: utf-8

# # installing snowflake connector
# 

# In[1]:


pip install snowflake-connector-python 


# # importing snowflake connector 

# In[ ]:


import snowflake.connector
import pandas as  pd


# # creating connection using snowflake connector

# In[7]:


cnn=snowflake.connector.connect(
    user='younusdar',
    password='**************',
    account='lb16366.europe-west4.gcp',
    warehouse='COMPUTE_WH_CAR',
    database='INSUR_DATABASE',
    schema='CAR_INSURANCE'
    )


# In[74]:


#pip install "snowflake-connector-python[pandas]"


# In[10]:


cs=cnn.cursor()


# In[63]:


#sql=cs.execute("select * ;")
sql=cs.execute("select * from CAR_INSURANCE_TABLE;")


# In[68]:


sql.fetchall()


# # calling procedure avg_car_val

# In[76]:


res = cs.execute(
    "call avg_car_val();"
    #"call avg_income_();"
    )
#
res.fetchall()


# In[ ]:





# # calling procedure avg_incom

# In[77]:


res1 = cs.execute(
    #"call avg_car_val();"
    "call avg_income_();"
    )
#
res1.fetchall()


# In[ ]:





# In[ ]:





# # fetching updated tables

# In[78]:



list = cs.execute(
    "SELect * from avg_car_val;"
    )

list.fetchall()


# In[81]:


list1 = cs.execute(
    "SELect * from avg_incom;"
    )

list1.fetchall()


# In[ ]:




