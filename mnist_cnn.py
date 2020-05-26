#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing dataset
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils


# In[2]:


# loading mnist data
dataset = mnist.load_data('mymnist.db')
train, test = dataset
X_train, y_train = train
X_test, y_test = test


# In[3]:


# Flattening images to a vector
img_shape = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape((X_train.shape[0], img_shape)).astype('float32')
X_test = X_test.reshape((X_test.shape[0], img_shape)).astype('float32')


# In[4]:


# Normalizing inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255


# In[5]:


# One-hot encoding
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)


# In[6]:


num_classes = y_test.shape[1]


# In[7]:


# define baseline model
def mnist_model():
    model = Sequential()
    model.add(Dense(img_shape, input_dim=img_shape, kernel_initializer='normal', activation='relu'))
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# In[8]:


# build the model
model = mnist_model()


# In[9]:


# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=200, verbose=0)


# In[10]:


# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy:  %.2f%%" % (scores[1]*100))


# In[ ]:




