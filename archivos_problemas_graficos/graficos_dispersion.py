import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dispersion.csv")
print(df)

#creando el gráfico
sns.scatterplot(x="tiempo", y="dinero", data=df)
plt.show()


#se maneja en simultaneo, mientras mas ventas hay mas dinero hay,

#mientaras mas tiempo se invierte mas dinero se gana y eso crea puntos en la grafica. 