import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# Function to compute the simplified expression
def compute_expression(k, Omega, p, terms=10):
    result = 0.0

    for n in range(1, terms + 1):
        for m in range(0, terms + 1):
            term = ((-1) ** (n - 1) / (n * np.log(2))) * ((-1) ** m / np.math.factorial(m)) * 0.5 * gamma((n + 1) / 2) * (Omega / (k + 1)) ** ((m + n + 1) / 2) * p ** n
            result += term

    return result

# Parameters
k_val = 1.0
Omega_val = 2.0
p_val = 0.5

# Number of terms in the series
num_terms = 10

# Compute the expression for different values of p
p_values = np.linspace(0.1, 2.0, 100)
result_values = [compute_expression(k_val, Omega_val, p, num_terms) for p in p_values]

# Plotting
plt.plot(p_values, result_values, label=f'k={k_val}, Omega={Omega_val}')
plt.title('Approximate Expression vs. p')
plt.xlabel('p')
plt.ylabel('Approximate Expression Value')
plt.legend()
plt.show()
