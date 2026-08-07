# Perform a Chi-Square Test

from scipy.stats import chi2_contingency

# Contingency Table
data =[[50, 30, 20], [30, 40, 30]]

# Perform Chi_Square Test
chi2, p, dof, expected = chi2_contingency(data)
print("Chi-Square Statistic:", chi2)
print("P-Values:", p)
print("Expected Frequencies: \n",expected)    