import pandas as pd

from sklearn import model_selection, linear_model, metrics, preprocessing


def evaluate(x, y):
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, shuffle=False)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_predicted = model.predict(x_test)

    error = metrics.mean_squared_error(y_test, y_predicted)
    score = model.score(x_test, y_test)

    print(f"Błąd średniokwadratowy: {error}")
    print(f"Score: {score}")


data = pd.read_csv('project-data/winequality-red.csv', sep=';', header=0, usecols=['alcohol', 'quality'])

evaluate(pd.DataFrame(data['alcohol']), pd.DataFrame(data['quality']))

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(data)
normalized = pd.DataFrame(np_scaled, columns=data.columns)

evaluate(pd.DataFrame(normalized['alcohol']), pd.DataFrame(normalized['quality']))
