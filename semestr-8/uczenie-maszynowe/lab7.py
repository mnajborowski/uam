import numpy as np
import pandas
import pandas as pd
from sklearn import model_selection, linear_model, metrics, preprocessing

data = pd.read_csv('lab7-data/flats.tsv', header=0, sep='\t',
                   usecols=['cena', 'Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe',
                            'Liczba pięter w budynku', 'Piętro', 'Typ zabudowy', 'Materiał budynku',
                            'Rok budowy', 'Forma własności', 'Stan', 'Stan instalacji', 'Głośność',
                            'Droga dojazdowa'])

data['Miejsce parkingowe'] = data['Miejsce parkingowe'].apply(
    lambda x: False if x == ' brak miejsca parkingowego' else True)
data.rename(columns={'Miejsce parkingowe': 'Czy miejsce parkingowe?'}, inplace=True)

data['Piętro'] = data['Piętro'].apply(lambda x: 0 if x in [' parter', ' niski parter'] else x)
data['Piętro'] = data['Piętro'].apply(pandas.to_numeric, errors='coerce')

data = pandas.get_dummies(data, columns=['Typ zabudowy', 'Materiał budynku'])

data['Forma własności'] = data['Forma własności'].apply(lambda x: True if x == ' własność' else False)
data.rename(columns={'Forma własności': 'Czy na własność?'}, inplace=True)

data['Stan'] = data['Stan'].apply(
    lambda x: True if x in [' do remontu', ' do rozbiórki', ' do odświeżenia', ' do wykończenia',
                            ' stan surowy zamknięty'] else False)
data.rename(columns={'Stan': 'Czy wymaga prac?'}, inplace=True)

data['Stan instalacji'] = data['Stan instalacji'].apply(lambda x: True if x == ' nowa' else False)
data.rename(columns={'Stan instalacji': 'Czy nowa instalacja?'}, inplace=True)

data['Głośność'] = data['Głośność'].apply(lambda x: True if x == ' ciche' else False)
data.rename(columns={'Głośność': 'Czy cicho?`'}, inplace=True)

data['Droga dojazdowa'] = data['Droga dojazdowa'].apply(lambda x: True if x is not np.nan else False)
data.rename(columns={'Droga dojazdowa': 'Czy droga dojazdowa?'}, inplace=True)

data = data.dropna()

X = data.drop('cena', axis=1)
y = data['cena']

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, shuffle=False)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

y_predicted = model.predict(x_test)

error = metrics.mean_squared_error(y_test, y_predicted)
score = model.score(x_test, y_test)

print(f"Błąd średniokwadratowy: {error}")
print(f"Score: {score}")

no_outliers = data.loc[(data['Powierzchnia w m2'] <= 200)]
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(no_outliers)
normalized = pd.DataFrame(np_scaled, columns=no_outliers.columns)

X = normalized.drop('cena', axis=1)
y = normalized['cena']

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, shuffle=False)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

y_predicted = model.predict(x_test)

error = metrics.mean_squared_error(y_test, y_predicted)
score = model.score(x_test, y_test)

print(f"Błąd średniokwadratowy po optymalizacji: {error}")
print(f"Score po optymalizacji: {score}")