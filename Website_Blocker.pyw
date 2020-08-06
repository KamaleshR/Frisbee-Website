#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


from datetime import datetime as dt


# In[3]:


hostpath="C:\Windows\System32\drivers\etc\hosts"


# In[4]:


redirect="127.0.0.1"
webToBlock=["www.facebook.com","facebook.com"]


# In[ ]:


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("WORKING HOURS")
        with open(hostpath,'r+')as file:
            cont=file.read()
            for w in webToBlock:
                if w in cont:
                    pass
                else:
                    file.write(redirect+" "+w+"\n")
    else:
        print("NON-WORKING HOURS")
        with open(hostpath,'r+')as file:
            cont=file.readlines()
            file.seek(0)
            for l in cont:
                if not any(w in l for w in webToBlock):
                    file.write(l)
                file.truncate()
    time.sleep(60)


# In[ ]:




