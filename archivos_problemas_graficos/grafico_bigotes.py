import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#leyebdo el dato
df = pd.read_csv("bigotes.csv")
print(df)

#creando el gráfico
sns.boxplot(x="categoria", y="valor", data=df)
plt.show()