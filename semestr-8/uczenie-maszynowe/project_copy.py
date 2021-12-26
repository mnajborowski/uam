import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

data = pd.read_csv('project-data/winequality-red.csv', sep=';', header=0, usecols=['alcohol', 'quality'])

X = data['alcohol']
y = data['quality']

train_dataset = data.sample(frac=0.8, random_state=0)
test_dataset = data.drop(train_dataset.index)

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('quality')
test_labels = test_features.pop('quality')

normalizer = preprocessing.Normalization(axis=None, input_shape=[1, ])
X_normalizer = preprocessing.Normalization(input_shape=[1, ], axis=None)
X_normalizer.adapt(X)

model = tf.keras.Sequential([
    X_normalizer,
    layers.Dense(units=1)
])
model.summary()
model.compile(
    optimizer=tf.optimizers.Adam(learning_rate=0.1),
    loss='mean_absolute_error')

history = model.fit(
    train_features, train_labels,
    epochs=100,
    verbose=0,
    validation_split=0.2)

test_results = {'model': model.evaluate(
    test_features,
    test_labels, verbose=0)}

print(test_results)

px = tf.linspace(0.0, 16, 10)
py = model.predict(px)

plt.scatter(train_features, train_labels, label='Data')
plt.plot(px, py, color='k', label='Predictions')
plt.xlabel('alcohol')
plt.ylabel('quality')
plt.legend()
plt.show()