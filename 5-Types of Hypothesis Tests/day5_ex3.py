from scipy.stats import f_oneway

# Date for groups
group1 = [10, 12, 14, 16, 18]
group2 = [9, 11, 13, 15, 17]
group3 = [8, 10, 12, 14, 16]

# Perform ANOVA
f_stat, p_value = f_oneway(group1, group2, group3)
print("F-Statistic:", f_stat)
print("P-Value:", p_value)