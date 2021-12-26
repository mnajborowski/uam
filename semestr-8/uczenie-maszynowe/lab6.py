import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures

data = pd.read_csv('lab6-data/data6.tsv', header=None, sep='\t')

x = pd.DataFrame(data[0])
y = pd.DataFrame(data[1])

x_seq = np.linspace(x.min(), x.max(), 300).reshape(-1, 1)
x_vector = np.array(x).reshape(-1, 1)

coefs1 = np.polyfit(x.values.flatten(), y.values.flatten(), 1)
plt.figure()
plt.plot(x_seq, np.polyval(coefs1, x_seq), color="red")
plt.title("Regression, degree = " + str(1))
plt.scatter(x, y)
plt.show()

coefs2 = np.polyfit(x.values.flatten(), y.values.flatten(), 2)
plt.figure()
plt.plot(x_seq, np.polyval(coefs2, x_seq), color="red")
plt.title("Regression, degree = " + str(2))
plt.scatter(x, y)
plt.show()

coefs5 = np.polyfit(x.values.flatten(), y.values.flatten(), 5)
plt.figure()
plt.plot(x_seq, np.polyval(coefs5, x_seq), color="red")
plt.title("Regression, degree = " + str(5))
plt.scatter(x, y)
plt.show()

# Zjawisko nadmiernego dopasowania wystepuje dla regresji 5. stopnia.

p_features5 = PolynomialFeatures(5, include_bias=False)
x1 = MinMaxScaler().fit_transform(x_vector)
x5 = p_features5.fit_transform(x1)
line5_reg = Ridge().fit(x5, data[1])
x_axis = np.arange(-0.1, 1, 0.01)

y5_reg = line5_reg.coef_[4] * x_axis ** 5 + line5_reg.coef_[3] * x_axis ** 4 + \
         line5_reg.coef_[2] * x_axis ** 3 + line5_reg.coef_[1] * x_axis ** 2 + \
         line5_reg.coef_[0] * x_axis + line5_reg.intercept_

plt.figure()
plt.plot(x_axis, y5_reg, color="red")
plt.title("Regression, degree = " + str(5) + ", regularized")
plt.scatter(x1, data[1])
plt.show()

# Zjawisko nadmiernego dopasowania po regularyzacji regresji 5. stopnia zostalo wyeliminowane.