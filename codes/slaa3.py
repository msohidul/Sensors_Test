import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define symbolic variables and parameters
x, k, p, Omega = sp.symbols('x k p Omega')
n, m = sp.symbols('n m', integer=True, positive=True)

# Define the series expansions
log_series = sp.Sum((-1)**(n-1) * (p*x)**n / (n * sp.log(2)), (n, 1, 100))
exp_series = sp.Sum((-1)**m / sp.factorial(m) * ((-1)*(k+1)*x**2/Omega)**m, (m, 0, 100))

# Define the Gaussian integral
gaussian_integral = 1/2 * sp.gamma((n + 1)/2) * ((Omega/(k+1))**((m + n + 1)/2)) * p**n

# Combine the series expansions and the Gaussian integral
integral_expression = sp.summation(sp.summation(gaussian_integral, (n, 1, 100)), (m, 0, 100))

# Evaluate the expression for a specific parameter
integral_result = integral_expression.subs({k: 1, p: 0.5, Omega: 2})

# Define a Python function for numerical evaluation
integral_function = sp.lambdify(x, integral_result, 'numpy')

# Generate x values for plotting
x_values = np.linspace(0, 5, 100)

# Evaluate the integral function
result_values = integral_function(x_values)

# Plot the result
plt.plot(x_values, result_values)
plt.xlabel('x')
plt.ylabel('Integral Result')
plt.title('Plot of the Integral Result')
plt.grid(True)
plt.show()
