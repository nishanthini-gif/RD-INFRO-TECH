import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df = df.drop("name",axis=1)

sns.heatmap(df.corr(),annot=True, cmap='coolwarm')
plt.title("Subject Correlation Heatmap")
plt.show()