import numpy as np
import pandas as pd
import random
from sklearn import model_selection, preprocessing, metrics

# Funkcja regresji logistcznej
from sklearn.linear_model import LogisticRegression


def h(theta, X):
    return 1.0 / (1.0 + np.exp(-X * theta))


# Funkcja kosztu dla regresji logistycznej
def j(h, theta, X, y):
    m = len(y)
    h_val = h(theta, X)
    s1 = np.multiply(y, np.log(h_val))
    s2 = np.multiply((1 - y), np.log(1 - h_val))
    return -np.sum(s1 + s2, axis=0) / m


# Gradient dla regresji logistycznej
def dj(h, theta, X, y):
    return 1.0 / len(y) * (X.T * (h(theta, X) - y))


# Metoda gradientu prostego dla regresji logistycznej
def gd(h, fJ, fdJ, theta, X, y, alpha=0.01, eps=10 ** -3, maxSteps=10000):
    errorCurr = fJ(h, theta, X, y)
    errors = [[errorCurr, theta]]
    while True:
        # oblicz nowe theta
        theta = theta - alpha * fdJ(h, theta, X, y)
        # raportuj poziom błędu
        errorCurr, errorPrev = fJ(h, theta, X, y), errorCurr
        # kryteria stopu
        if abs(errorPrev - errorCurr) <= eps:
            break
        if len(errors) > maxSteps:
            break
        errors.append([errorCurr, theta])
    return theta, errors


# Funkcja decyzyjna regresji logistycznej
def classify_bi(theta, X):
    prob = h(theta, X).item()
    return (1, prob) if prob > 0.5 else (0, prob)


# Klasyfikator losowy
def classify_random(theta, X):
    prob = h(theta, X).item()
    return random.randint(0, 1), prob


# Skuteczność modelu
def count_acc(f_class, X_test, y_test):
    acc = 0.0
    for i, rest in enumerate(y_test):
        cls, prob = f_class(thetaBest, X_test[i])
        if i < 10:
            print(int(y_test[i].item()), "<=>", cls, "-- prob:", round(prob, 4))
        acc += cls == y_test[i].item()
    return acc


full_data = pd.read_csv('lab5-data/gratkapl-centrenrm.csv')
data = full_data[["Price", "Rooms", "SqrMeters", "Floor", "Centre"]]

no_outliers = data.loc[(data['Price'] < 29000000) & (data['SqrMeters'] < 180)]

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(no_outliers)
normalized = pd.DataFrame(np_scaled, columns=no_outliers.columns)

m, n_plus_1 = normalized.values.shape
n = n_plus_1 - 1
X_n = normalized.values[:, 0:n].reshape(m, n)

X = np.matrix(np.concatenate((np.ones((m, 1)), X_n), axis=1)).reshape(m, n_plus_1)
y = np.matrix(no_outliers.values[:, n]).reshape(m, 1)
X_scaled = X / np.amax(X, axis=0)

x_train, x_test, y_train, y_test = model_selection.train_test_split(X_scaled, y, test_size=0.2, shuffle=False)

thetaTemp = np.ones(5).reshape(5, 1)
thetaBest, errors = gd(h, j, dj, thetaTemp, x_train, y_train,
                       alpha=0.1, eps=10 ** -7, maxSteps=1000)

print("theta =", thetaBest)
print("x0 =", x_test[0])
print("h(x0) =", h(thetaBest, x_test[0]).item())
print("c(x0) =", classify_bi(thetaBest, x_test[0]), "\n")

print("\nAccuracy:", count_acc(classify_bi, x_test, y_test) / len(x_test))
print()
print("\nRandom classifier accuracy:", count_acc(classify_random, x_test, y_test) / len(x_test))

model = LogisticRegression()
model.fit(x_train, y_train)

y_predicted = model.predict(x_test)

precision, recall, fscore, support = metrics.precision_recall_fscore_support(y_test, y_predicted, average="micro")
print()
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F-score: {fscore}")

