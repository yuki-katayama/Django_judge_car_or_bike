import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.optimizers import SGD,Adam
from keras.utils import np_utils

classes = ["car", "motorbile"]
num_classes = len(classes)
image_size = 150

X_train, X_test, y_train, y_test = np.load("./imagefiles.npy", allow_pickle=True)
y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32, (3,3), activation = "relu", input_shape = (image_size, image_size,3)))
model.add(Conv2D(32,(3,3), activation = "relu"))
model.add(MaxPool2D(pool_size = (2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3), activation = "relu"))
model.add(Conv2D(64,(3,3), activation = "relu"))
model.add(MaxPool2D(pool_size = (2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation="softmax"))

# opt = SGD(lr = 0.01)
opt = Adam()
model.compile(loss = "categorical_crossentropy", optimizer = opt,metrics=["accuracy"])

model.fit(X_train, y_train, batch_size =32, epochs = 20)
score = model.evaluate(X_test, y_test, batch_size = 32)

