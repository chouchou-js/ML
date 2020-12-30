import tensorflow as tf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    print(x_train.shape)
    print(y_train.shape)
    print(x_test.shape)
    print(y_test.shape)

    image = x_train[1]
    # print(x_train[1])
    print(y_train[1])

    fig = plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()
