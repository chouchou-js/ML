import os
import tensorflow as tf
import matplotlib.pyplot as plt
cifar10 = tf.keras.datasets.cifar10


# 데이터 저장 경로
save_dir = '../data'
save_photo_dir = '../data/photo'
if not os.path.exists(save_photo_dir):
    os.makedirs(save_photo_dir)

# 데이터 불러오기
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 데이터 변환
x_train, x_test = x_train / 255.0, x_test / 255.0

# 데이터 라벨링
categories = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# 모델 불러오기
# tf.keras.models.load_model(f'{save_dir}/cifar10.h5')

# 모델 정의
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, 3, input_shape=x_train.shape[1:], activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Conv2D(64, 3, activation='relu'),

    tf.keras.layers.Conv2D(64, 3),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Dense(len(categories), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 훈련
model.fit(x_train, y_train, batch_size=64, epochs=5)

# 평가
model.evaluate(x_test, y_test)

# 예측 & 출력
prd = model.predict(x_test)
for i, v in enumerate(prd):
    predicted_y = v.argmax()
    real_y = y_test[i][0]

    if predicted_y != real_y:
        plt.figure()
        plt.suptitle(f'''predicted: {categories[predicted_y]}, real: {categories[real_y]}''',
                     fontsize=20, fontweight='bold')
        plt.imshow(x_test[i])
        plt.savefig(f'{save_photo_dir}/{i}.png')
        plt.close()

# 모델 저장
model.save(f'{save_dir}/cifar10.h5')
