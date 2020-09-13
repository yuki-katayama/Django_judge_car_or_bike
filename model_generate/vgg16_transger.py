import numpy as np
from tensorflow import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.optimizers import SGD,Adam
from keras.utils import np_utils
from keras.applications import VGG16

classes = ["car", "motorbile"]
num_classes = len(classes)
image_size = 224

X_train, X_test, y_train, y_test = np.load("./imagefiles_224.npy", allow_pickle=True)
y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)
X_train = X_train.astype("float") /255.0
X_test = X_test.astype("float")/255.0

model = VGG16(weights = "imagenet", include_top = False, input_shape = (image_size, image_size, 3))
# print("Model loaded")
# model.summary()

top_model = Sequential()
top_model.add(Flatten(input_shape = model.output_shape[1:]))
top_model.add(Dense(256, activation="relu"))
top_model.add(Dense(num_classes, activation = "softmax"))

model = Model(inputs = model.input, outputs = top_model(model.output))
# model.summary()
for layer in model.layers[:15]:
    layer.trainable = False


# opt = SGD(lr = 0.01)
opt = Adam(lr = 0.0001)
model.compile(loss = "categorical_crossentropy", optimizer = opt,metrics=["accuracy"])

model.fit(X_train, y_train, batch_size =32, epochs = 17)
score = model.evaluate(X_test, y_test, batch_size = 32)

model.save("./vgg16_transfer.h5")