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


# Number of output classes
num_classes = y_test.shape[1]


# In[7]:


# define mnist model
def mnist_model(neuron):
    model = Sequential()
    model.add(Dense(neuron, input_dim=img_shape, kernel_initializer='normal', activation='relu'))
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# In[8]:


# build the model
neuron = 5
model = mnist_model(neuron)
accuracy = 0.0

def fit_model():
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=200, verbose=0)
    scores = model.evaluate(X_test, y_test, verbose=0)
    accuracy = scores[1]*100
    print("Accuracy: %.2f%%" % (scores[1]*100))
    return accuracy


# In[9]:


fit_model()
count = 0
best_acc = accuracy
best_neuron = 0


# In[10]:


def resetWeights():
    print("Reseting weights")
    w = model.get_weights()
    w = [[j*0 for j in i] for i in w]
    model.set_weights(w)


# In[11]:


while accuracy < 99 and count < 4:
    print("Updating Model")
    model = mnist_model(neuron*2)
    neuron = neuron * 2
    count = count + 1
    accuracy = fit_model()
    if best_acc < accuracy:
        best_acc = accuracy
        best_neuron = neuron
    print()
    resetWeights()


# In[12]:


print(best_neuron)
model = mnist_model(best_neuron)
fit_model()
model.save('mnist_model_update.h5')
print("Model Saved")


# In[13]:


file1 = open("result.txt","w")
file1.write(str(best_acc))
file1.close()


# In[ ]:




