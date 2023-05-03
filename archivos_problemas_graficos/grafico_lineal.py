import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas.csv")
print(df)
sns.lineplot(x="fecha", y="pedos", data=df)
plt.show()