import pandas as pd

from sklearn import model_selection, linear_model, metrics

data = pd.read_csv('lab5-data/fires_thefts.csv', header=None)

fires = pd.DataFrame(data[0])
thefts = pd.DataFrame(data[1])

x_train, x_test, y_train, y_test = model_selection.train_test_split(fires, thefts, test_size=0.2, shuffle=False)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

y_predicted = model.predict(x_test)

error = metrics.mean_squared_error(y_test, y_predicted)
score = model.score(x_test, y_test)

print(f"Błąd średniokwadratowy: {error}")
print(f"Score: {score}")
