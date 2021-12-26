import numpy as np
import pandas
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def batch_iterate(x, y, batch_size):
    assert len(x) == len(y)
    dataset_size = len(x)
    current_index = 0
    while current_index < dataset_size:
        x_batch = x[current_index: current_index + batch_size]
        y_batch = y[current_index: current_index + batch_size]
        yield x_batch, y_batch
        current_index += batch_size


data = pd.read_csv('lab8-data/mushrooms.tsv', sep='\t', names=[
    'edibility',
    'cap-shape',
    'cap-surface',
    'cap-color',
    'bruises?',
    'odor',
    'gill-attachment',
    'gill-spacing',
    'gill-size',
    'gill-color',
    'stalk-shape',
    'stalk-root',
    'stalk-surface-above-ring',
    'stalk-surface-below-ring',
    'stalk-color-above-ring',
    'stalk-color-below-ring',
    'veil-type',
    'veil-color',
    'ring-number',
    'ring-type',
    'spore-print-color',
    'population',
    'habitat',
])

data['edibility'] = data['edibility'].apply(lambda x: 0 if x == 'p' else 1)
data.rename(columns={'edibility': 'edible?'}, inplace=True)

data['cap-color'] = data['cap-color'].apply(lambda x: 1 if x == 'e' else 0)
data.rename(columns={'cap-color': 'red-cap?'}, inplace=True)

data['bruises?'] = data['bruises?'].apply(lambda x: 1 if x == 't' else 0)

data['spore-print-color'] = data['spore-print-color'].apply(lambda x: 1 if x == 'w' else 0)
data.rename(columns={'spore-print-color': 'white-spore-print-color?'}, inplace=True)

data = pandas.get_dummies(data, columns=['cap-shape', 'odor', 'population', 'habitat'])

features = ['cap-shape_b', 'cap-shape_c', 'cap-shape_f', 'cap-shape_k',
            'cap-shape_s', 'cap-shape_x', 'red-cap?', 'white-spore-print-color?']

X = data[features]
y = data['edible?']

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, shuffle=False)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)

model = SGDClassifier()
batch_iterator = batch_iterate(x_train_scaled, y_train, batch_size=100)
for x_batch, y_batch in batch_iterator:
    model.partial_fit(x_batch, y_batch, classes=np.unique(y_train))

y_predicted = model.predict(x_test)

error = mean_squared_error(y_test, y_predicted)
score = model.score(x_test, y_test)

print(f"Błąd średniokwadratowy: {error}")
print(f"Score: {score}")

features_more = ['red-cap?', 'bruises?', 'white-spore-print-color?',
                 'cap-shape_b', 'cap-shape_c', 'cap-shape_f', 'cap-shape_k',
                 'cap-shape_s', 'cap-shape_x', 'odor_a', 'odor_c', 'odor_f', 'odor_l',
                 'odor_m', 'odor_n', 'odor_p', 'odor_s', 'odor_y', 'population_a',
                 'population_c', 'population_n', 'population_s', 'population_v',
                 'population_y', 'habitat_d', 'habitat_g', 'habitat_l', 'habitat_m',
                 'habitat_p', 'habitat_u', 'habitat_w']

X = data[features_more]
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, shuffle=False)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)

model = SGDClassifier()
batch_iterator = batch_iterate(x_train_scaled, y_train, batch_size=100)
for x_batch, y_batch in batch_iterator:
    model.partial_fit(x_batch, y_batch, classes=np.unique(y_train))

y_predicted = model.predict(x_test)

error = mean_squared_error(y_test, y_predicted)
score = model.score(x_test, y_test)

print(f"Błąd średniokwadratowy z modelem wytrenowanym po większej liczbie cech: {error}")
print(f"Score z modelem wytrenowanym po większej liczbie cech: {score}")
