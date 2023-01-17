from scipy.optimize import curve_fit
import numpy as np

# Define the Svensson function
def svensson(t, beta0, beta1, beta2, lambda1, lambda2):
    return beta0 + beta1 * (1 - np.exp(-lambda1 * t)) / (lambda1 * t) + beta2 * ((1 - np.exp(-lambda1 * t)) / (lambda1 * t) - np.exp(-lambda1 * t)) + lambda2 * (1 - np.exp(-lambda2 * t))

# Generate some sample data
maturity = np.array([1, 2, 3, 5, 7, 10, 20, 30])
yields = np.array([0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09])

# Define the initial values for the parameters
p0 = [0.02, 0.03, 0.04, 0.05, 0.06]

# Calibrate the model
params, _ = curve_fit(svensson, maturity, yields, p0)

# Print the calibrated parameters

print(params)