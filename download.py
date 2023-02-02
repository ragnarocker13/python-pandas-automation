#!/usr/bin/env python
# coding: utf-8

# In[34]:


from selenium import webdriver
from selenium.webdriver.common.by import By


# In[35]:


# Set chromedriver options
options = webdriver.ChromeOptions()

preferences = {"download.default_directory": "C:\pythonTest", "safebrowsing.enabled":"false"}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(chrome_options=options)

# Load URL and click download link by link text
driver.get("https://jobs.homesteadstudio.co/data-engineer/assessment/download/")
driver.find_element(By.LINK_TEXT, "Download").click()


# In[ ]:




