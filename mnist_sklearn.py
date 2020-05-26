#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Import model
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# In[16]:


# Importing dataset
digits = load_digits()
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)


# In[17]:


# Model building
model = KNeighborsClassifier()
model.fit(x_train, y_train)


# In[18]:


# Prediction
pred = model.predict(x_test)


# In[19]:


# Finding Accuracy
accu = model.score(x_test, y_test)
print("Accuracy:  %.2f%%" % (accu*100))


# In[20]:


file = open("result.txt","w")
file.write(str(score))


# In[ ]:




