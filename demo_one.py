import tensorflow as tf

'''
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
result = tf.matmul(matrix1, matrix2)
with tf.Session() as sess:
    product = sess.run(result)
    print product.dtype
'''

'''
sess = tf.InteractiveSession()
x = tf.Variable([1., 2.])
a = tf.constant([3., 3.])
x.initializer.run()
sub = tf.sub(x, a)
print sub.eval()
'''

state = tf.Variable(0, name = "counter")
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)
init_op = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init_op)
    print sess.run(state)
    for _ in range(3):
        print sess.run(update)
        print sess.run(state)
