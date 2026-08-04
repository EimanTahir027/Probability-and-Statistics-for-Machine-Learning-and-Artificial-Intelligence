import numpy as np
from scipy.stats import norm, t

# Sample Data
data = [12, 14, 15, 16, 17, 18, 19]

# Calculate mean and standard deviation
mean = np.mean(data)
std = np.std(data, ddof=1)

# 95% Confidence Interval (using t-distribution)
n = len(data)
t_value = t.ppf(0.975, df=n-1)
margin_of_error = t_value * (std / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error) 
print("95% COnfidence Interval: ", ci)