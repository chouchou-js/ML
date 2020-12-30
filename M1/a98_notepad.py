import tensorflow as tf
import tensorflow.keras.layers as layers
import tensorflow.keras.optimizers as optimizers
import tensorflow.keras.utils as utils

if __name__ == '__main__':
    # 데이터 로드
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # 데이터 변환
    x_train = x_train.reshape(60000, 784).astype('float32')
    x_test = x_test.reshape(10000, 784).astype('float32')
    x_train /= 255
    x_test /= 255

    # 데이터 레이블
    y_train = utils.to_categorical(y_train, 10)
    y_test = utils.to_categorical(y_test, 10)

    # 모델 정의
    model = tf.keras.models.Sequential()
    model.add(layers.Dense(512, input_shape=(784,)))
    model.add(layers.Activation('relu'))
    model.add(layers.Dense(10))
    model.add(layers.Activation('softmax'))

    # 모델 구축
    model.compile(
        loss='categorical_crossentropy',
        optimizer=optimizers.Adam(),
        metrics=['accuracy']
    )

    # 훈련
    hist = model.fit(x_train, y_train)

    # 평가
    score = model.evaluate(x_test, y_test, verbose=1)
    print(f'loss = {score[0]}')
    print(f'accuracy = {score[1]}')
