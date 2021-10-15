from flask import Flask
import keras as k
import tensorflow as tf
import numpy as np
from sklearn.datasets import load_digits
from keras.models import Sequential
from keras.layers import Dense, Input
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)


@app.route('/')
def index():
    return 'Example Landing Page.'


@app.route('/predict')
def predict():
    model = k.models.load_model('digits_classifier.h5')
    y_pred = model.predict(X_test)
    y_pred = np.argmax(y_pred, axis=1)
    acc = accuracy_score(np.argmax(y_test, axis=1), y_pred)
    return f'Correctly identified {acc:.3f} percent of images in X_test.'


@app.route('/train')
def train():
    model_name = 'digits_classifier.h5'
    model = Sequential()
    model.add(Input(shape=X_train.shape[1], name='Input_Layer'))
    model.add(Dense(32, activation='relu', name='First_Layer'))
    model.add(Dense(16, activation='relu', name='Second_Layer'))
    model.add(Dense(y_train.shape[1], activation='softmax', name='Output_Layer'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['acc'])

    model.fit(X_train, y_train, batch_size=350, validation_split=0.3, epochs=200, verbose=1)
    model.save(model_name)
    return f'Saved model {model_name} to disk.'


# data prep is done only once and with set random_state to ensure reproducibility:
digits = load_digits()
X, y = digits.images, digits.target

X = X.reshape(X.shape[0], X.shape[1] * X.shape[2])
X = X / np.amax(X)

y = tf.keras.utils.to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42, stratify=y)
