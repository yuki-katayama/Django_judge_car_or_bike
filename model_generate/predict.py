import numpy as np
from tensorflow import keras
from keras.models import Sequential, Model, load_model
from PIL import Image
import sys

classes = ["car", "motorbike"]
num_classes = len(classes)
image_size = 224

image = Image.open(sys.argv[1])
image = image.convert("RGB")
image = image.resize((image_size, image_size))
data = np.asarray(image) / 255.0

X = []
Y = []

X.append(data)
X = np.array(X)

model = load_model("./vgg16_transfer.h5")

result = model.predict([X])[0]
predicted = result.argmax()
percentage = int(result[predicted] * 100)
print(classes[predicted], percentage)