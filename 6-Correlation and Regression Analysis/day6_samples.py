from sklearn.linear_model import LinearRegression
import numpy as np

# Sample Data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 8, 10])

# Fit Linear Regression
model = LinearRegression()
model.fit(x, y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("R-Squared: ", model.score(x, y))