from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
from keras.datasets import mnist
from keras.utils import np_utils
import keras
import sys


(x_train, y_train), (x_test, y_test)  = mnist.load_data()

img_rows = x_train[0].shape[0]
img_cols = x_train[1].shape[0]

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]
num_pixels = x_train.shape[1] * x_train.shape[2]

# Model Creation

model = Sequential()

# Adding layers to model

def input_layers(conv,nfilter,filter_size,pool_size,fc_input,no_neurons):
    #conv = int(input('conv layers :'))
    #nfilter = int(input('filter layer :'))
    #filter_size = int(input('filter size :'))
    #pool_size = int(input('pool layer :'))
    this_layer = 'No. of convolve layers : ' + str(conv)
    this_layer = this_layer + '\nLayer 1'
    this_layer = this_layer + '\nNo of filters : ' + str(nfilter) + '\nFilter Size : ' + str(filter_size) + '\nPool Size : ' + str(pool_size)

    model.add(Conv2D(nfilter, (filter_size,filter_size),padding = "same",input_shape = input_shape))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size = (pool_size,pool_size)))

    for i in range(1,conv):
        nfilters = int(input('filters layers :'))
        filter_size = int(input('filters size :'))
        pool_size = int(input('pool size :'))
        this_layer = this_layer + '\nLayer ' + str(i+1) + ': '
        this_layer = this_layer + '\nNo of filters : ' + str(nfilters) + '\nFilter Size : ' + str(filter_size) + '\nPool Size : ' + str(pool_size)
        model.add(Conv2D(nfilters, (filter_size, filter_size),padding = "same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size = (pool_size, pool_size)))

    model.add(Flatten())

    this_layer = this_layer + '\nNo. of FC Layers : ' + str(fc_input+1) 

    for i in range(0,fc_input):
        #no_neurons = int(input('neurons :'))
        this_layer = this_layer + '\nNeurons in Layer ' + str(i+1) + ' : ' + str(no_neurons)
        model.add(Dense(no_neurons))
        model.add(Activation("relu"))

    model.add(Dense(num_classes))
    model.add(Activation("softmax"))
           
    this_layer = this_layer + '\nNeurons in Layer ' + str(fc_input + 1) + ' : ' + str(num_classes)

    model.compile(loss = 'categorical_crossentropy',
                  optimizer = keras.optimizers.Adadelta(),
                  metrics = ['accuracy'])
    
    print(model.summary())

input_layers(1,64,3,3,0,32)

# Training the model 

def training():
    batch_size = 128
    epochs = 5
    
    history = model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_data=(x_test, y_test),
              shuffle=True)
    model.save("mlops.h5")

    global scores
    scores = model.evaluate(x_test, y_test, verbose=1)
    print('Test loss:', scores[0])
    print('Test accuracy:', scores[1])


training()

# Retraining the model

if scores[1] < 0.95 :
    input_layers(2,64,3,3,1,32)
    training()
    
 # Save accuracy to particular file

accuracy_file = open('/MLops/accuracy.txt','w')
accuracy_file.write(str(scores[1]))
accuracy_file.close()
