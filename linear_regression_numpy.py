import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
Y = 4 + 3 * X + np.random.randn(100, 1)

# Linear Regression using the Normal Equation
X_b = np.c_[np.ones((100, 1)), X]  # add x0 = 1 to each instance
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)

print("Intercept:", theta_best[0][0])
print("Slope:", theta_best[1][0])

# Predict values
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
Y_predict = X_new_b.dot(theta_best)

# Plot
plt.plot(X_new, Y_predict, "r-", label="Prediction")
plt.scatter(X, Y, label="Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
