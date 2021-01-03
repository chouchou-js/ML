import tensorflow as tf
import matplotlib.pyplot as plt


cifar10 = tf.keras.datasets.cifar10

# 데이터 불러오기
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

print(x_train[0])
print(y_train[0])

image = x_train[0]
plt.imshow(image)
plt.show()
