import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

del df["species"]

# Compute correlation matrix
correlation_matrix = df.corr()

# Plot Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Feature Correlations")
plt.show()