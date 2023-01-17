from scipy.optimize import curve_fit
import numpy as np

# Define the Svensson function
def svensson(t, beta0, beta1, beta2, beta3, lambda1, lambda2):
    return beta0 + beta1*(1-np.exp(-lambda1*t))/(lambda1*t) + beta2*((1-np.exp(-lambda1*t))/(lambda1*t) - np.exp(-lambda1*t)) + beta3*(1-np.exp(-lambda2*t))

# Generate some sample data
maturity = np.array([1, 2, 3, 5, 7, 10, 20, 30])
yields = np.array([0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09])

# Define the initial values for the parameters
p0 = [0.02, 0.03, 0.04, 0.05, 0.1, 0.15]

# Calibrate the model
params, _ = curve_fit(svensson, maturity, yields, p0)

# Print the calibrated parameters
print(params)




# with parameters limitations



from scipy.optimize import minimize
import numpy as np

# Define the Svensson function
def svensson(params, t):
    beta0, beta1, beta2, beta3, lambda1, lambda2 = params
    return beta0 + beta1*(1-np.exp(-lambda1*t))/(lambda1*t) + beta2*((1-np.exp(-lambda1*t))/(lambda1*t) - np.exp(-lambda1*t)) + beta3*(1-np.exp(-lambda2*t))

# Generate some sample data
maturity = np.array([1, 2, 3, 5, 7, 10, 20, 30])
yields = np.array([0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09])

# Define the initial values for the parameters
p0 = [0.02, 0.03, 0.04, 0.05, 0.1, 0.15]


# Define the constraints
constraints = (
    {'type': 'ineq', 'fun': lambda x: x[0]}, #beta0 > 0
    {'type': 'ineq', 'fun': lambda x: x[1]-0.05}, #beta1 > 0.05
    {'type': 'ineq', 'fun': lambda x: x[0]+x[1]-0.07}, #beta0 + beta1 > 0.07
    {'type': 'ineq', 'fun': lambda x: x[2] + 1}, #beta2 > -1
    {'type': 'ineq', 'fun': lambda x: x[3] + 1}, #beta3 > -1
    {'type': 'ineq', 'fun': lambda x: x[4]}, #lambda1 > 0
    {'type': 'ineq', 'fun': lambda x: x[5]}, #lambda2 > 0
)

# Optimize the model
res = minimize(lambda params: np.sum((svensson(params, maturity) - yields)**2), p0, method='SLSQP', constraints=constraints)

# Print the optimized parameters
print(res.x)

