import tensorflow as tf

if __name__ == '__main__':
    c1 = tf.constant(10, name="first")
    c2 = tf.constant(20, name="first")
    v1 = tf.Variable(0)

    print(c1)
    print(v1)
