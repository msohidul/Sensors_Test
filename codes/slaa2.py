import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1
p = 2.15
omega_values = np.linspace(1, 10, 100)  # Adjust the number of points for smoother curves

# Function to evaluate the series expansion
def series_expression(omega):
    result = 0
    for n in range(1, 10):  # Considering the first 10 terms for simplicity
        for m in range(10):  # Considering the first 10 terms for simplicity
            result += ((-1)**(n + m - 1) * p**n) / (np.log(2) * omega**m) * (1 / ((n + m + 1)**2 * np.math.factorial(n * m)))
    return result

# Evaluate the expression for each omega value
results = [series_expression(omega) for omega in omega_values]

# Plotting
plt.plot(omega_values, results, label=r'Approximate Solution ($\sum_{n,m}$)', color='blue')
plt.xlabel('Average SNR (dB)')
plt.ylabel('Channel Capacity (bits/sec/Hz)')
plt.title('Capacity vs Average SNR')
plt.legend()
plt.show()
